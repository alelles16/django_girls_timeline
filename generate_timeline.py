from datetime import datetime
from dateutil.relativedelta import relativedelta
from constants import OPEN_ENROLLMENT, CLOSE_ENROLLMENT, SELECTION_PARTICIPANTS_INIT, \
    SELECTION_PARTICIPANTS_FINISH, ANNOUNCEMENT_OF_PARTICIPANTS, CONFIRMATION_LIMIT, \
    ANNOUNCEMENT_OF_PARTICIPANTS_ON_WAITING_LIST, CONFIRMATION_LIMIT_WAITING_LIST, \
    INSTALLATION_AND_PRESENTATION, EVENT_DAY


def generate_timeline():
    """
    Generate timeline for events based on specified days before the event day.
    """
    events = {
        'Inscripciones abiertas:': get_event_date(OPEN_ENROLLMENT),
        'Inscripciones cerradas:': get_event_date(CLOSE_ENROLLMENT),
        'Seleccion de participantes inicia:': get_event_date(SELECTION_PARTICIPANTS_INIT),
        'Seleccion de participantes finaliza:': get_event_date(SELECTION_PARTICIPANTS_FINISH),
        'Anuncio de participantes seleccionados:': get_event_date(ANNOUNCEMENT_OF_PARTICIPANTS),
        'Limite de confirmacion:': get_event_date(CONFIRMATION_LIMIT),
        'Anuncio participantes lista de espera:': get_event_date(ANNOUNCEMENT_OF_PARTICIPANTS_ON_WAITING_LIST),
        'Limite de confirmacion lista de espera:': get_event_date(CONFIRMATION_LIMIT_WAITING_LIST),
        'Reunion previa:': get_event_date(INSTALLATION_AND_PRESENTATION)
    }
    print_events(events)


def get_event_date(num_days):
    """
    Calculate the event date based on the specified number of days before the event day.
    """
    event_date = datetime.strptime(EVENT_DAY, "%d/%m/%Y")
    return (event_date - relativedelta(days=num_days)).strftime('%d %B, %Y')


def print_events(events):
    """
    Print events and their corresponding dates.
    """
    for event, date in events.items():
        print(f'{event} {date}\n')


if __name__ == "__main__":
    generate_timeline()
