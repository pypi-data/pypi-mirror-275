import ipih

from pih import A, PIHThread, send_message
from ReviewAutomationService.const import SD

SC = A.CT_SC

ISOLATED: bool = False


def start(as_standalone: bool = False) -> None:
    from datetime import datetime
    from pih.consts.errors import NotFound
    from pih.collections import (
        EventDS,
        PolibasePerson,
        WhatsAppMessage,
        PolibasePersonNotificationConfirmation as PPNC,
    )
    from ReviewAutomationService.api import (
        ReviewNotificationApi as Api,
    )
    from pih.tools import j, nn, ne, one, nnt, FullNameTool, ParameterList

    SENDER: str = A.D.get(A.CT_ME_WH_W.Profiles.MARKETER)

    def service_call_handler(sc: SC, pl: ParameterList) -> bool | None:
        if sc == SC.heart_beat:
            heat_beat_handler(A.D_Ex.parameter_list(pl).get())
            return True
        if sc == SC.send_event:
            event: A.CT_E = A.D_Ex_E.get(pl)
            if event == A.CT_E.WHATSAPP_MESSAGE_RECEIVED:
                message: WhatsAppMessage | None = A.D_Ex_E.whatsapp_message(pl)
                if ne(message):
                    sender: str = nnt(nnt(message).profile_id)
                    if sender == SENDER:
                        telephone_number: str = A.D_F.telephone_number_international(
                            nnt(nnt(message).sender)
                        )
                        notification_confirmation: PPNC | None = A.R_P_N_C.by(
                            telephone_number, sender
                        ).data

                        message_text: str | None = nnt(nnt(message).message)
                        if ne(message_text):
                            message_text = message_text.lower()
                            try:
                                person: PolibasePerson | None = one(
                                    A.R_P.person_by_telephone_number(telephone_number)
                                )
                                if (
                                    nn(person)
                                    and ne(notification_confirmation)
                                    and nnt(notification_confirmation).status == 2
                                ):
                                    yes_answer_variants: list[str] = A.S.get(
                                        A.CT_S.POLIBASE_PERSON_YES_ANSWER_VARIANTS
                                    )

                                    no_answer_variants: list[str] = A.S.get(
                                        A.CT_S.POLIBASE_PERSON_NO_ANSWER_VARIANTS
                                    )

                                    answer_yes: bool = A.D.has_one_of(
                                        message_text, yes_answer_variants
                                    )
                                    answer_no: bool = A.D.has_one_of(
                                        message_text, no_answer_variants
                                    )
                                    if answer_yes or answer_no:
                                        if A.A_P_N_C.update(
                                            telephone_number, sender, int(answer_yes)
                                        ):
                                            review_event: EventDS | None = one(
                                                A.R_E.get_last(
                                                    A.CT_E.POLIBASE_PERSON_REVIEW_NOTIFICATION_WAS_REGISTERED,
                                                    (nnt(person).pin,),
                                                )
                                            )
                                            is_inpatient: bool = (
                                                nnt(nnt(review_event).parameters)[
                                                    A.CT_PI.INPATIENT.name
                                                ]
                                                if nn(review_event)
                                                and nn(nnt(review_event).parameters)
                                                else False
                                            )
                                            if answer_yes:
                                                send_message(
                                                    str(
                                                        A.S.get(
                                                            A.CT_S.POLIBASE_PERSON_TAKE_REVIEW_ACTION_URL_TEXT
                                                        )
                                                    ).format(
                                                        name=FullNameTool.to_given_name(
                                                            nnt(nnt(person).FullName)
                                                        )
                                                    ),
                                                    telephone_number,
                                                    sender,
                                                    True,
                                                )
                                                send_message(
                                                    A.S.get(
                                                        A.CT_S.REVIEW_ACTION_URL_FOR_INPATIENT
                                                        if is_inpatient
                                                        else A.CT_S.REVIEW_ACTION_URL
                                                    ),
                                                    telephone_number,
                                                    sender,
                                                )
                                            else:
                                                send_message(
                                                    A.S.get(
                                                        A.CT_S.POLIBASE_PERSON_NO_ANSWER_ON_NOTIFICATION_CONFIRMATION_TEXT
                                                    ),
                                                    telephone_number,
                                                    sender,
                                                    True,
                                                )

                                            A.E.send(
                                                A.CT_E.POLIBASE_PERSON_REVIEW_NOTIFICATION_WAS_ANSWERED,
                                                (
                                                    nnt(person).pin,
                                                    j((message_text.splitlines())),
                                                    int(answer_yes),
                                                ),
                                            )
                                    else:
                                        pass
                            except NotFound as error:
                                A.L.debug_bot(
                                    j((SD.standalone_name, ": ", error.get_details()))
                                )
                        return True
        return None

    def heat_beat_handler(current_datetime: datetime) -> None:
        if A.S_P_RN.is_on():
            if A.D.is_equal_by_time(current_datetime, A.S_P_RN.start_time()):
                PIHThread(
                    Api.start_review_notification_distribution_action,
                )

    def service_starts_handler() -> None:
        A.SRV_A.subscribe_on(SC.heart_beat)
        A.SRV_A.subscribe_on(SC.send_event)

    A.SRV_A.serve(
        SD,
        service_call_handler,
        service_starts_handler,
        isolate=ISOLATED,
        as_standalone=as_standalone,
    )


if __name__ == "__main__":
    start()
