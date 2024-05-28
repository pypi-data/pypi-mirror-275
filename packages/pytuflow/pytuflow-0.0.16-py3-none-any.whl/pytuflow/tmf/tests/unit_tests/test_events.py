from tmf.tuflow_model_files.cf.tef import TEF
from tmf.tuflow_model_files.dataclasses.event import Event, EventDatabase


def test_event():
    event = Event('Q100', '_ARI_', '100y')
    assert event.name == 'Q100'
    assert event.variable == '_ARI_'
    assert event.value == '100y'
    assert repr(event) == '<Event> Q100: _ARI_ | 100y'
    assert str(event) == 'Q100: _ARI_ | 100y'


def test_event_eq():
    event1 = Event('Q100', '_ARI_', '100y')
    event2 = Event('Q100', '_ARI_', '100y')
    assert event1 == event2


def test_event_ne():
    event1 = Event('Q100', '_ARI_', '100y')
    event2 = Event('Q100', '_ARI_', '50y')
    assert event1 != event2


def test_event_ne2():
    event1 = Event('Q100', '_ARI_', '100y')
    event2 = Event('Q100CC', '_ARI_', '100y')
    assert event1 != event2


def test_event_ne3():
    event1 = Event('Q100', '_ARI_', '100y')
    event2 = 'Q100'
    assert event1 != event2


def test_event_database():
    event1 = Event('Q100', '_ARI_', '100y')
    event_database = EventDatabase({event1.name: event1})
    assert event_database['Q100'] == event1


def test_event_database_add():
    event1 = Event('Q100', '_ARI_', '100y')
    event2 = Event('Q100CC', '_ARI_', '100yCC')
    event_database = EventDatabase({event1.name: event1})
    event_database[event2.name] = event2
    assert event_database.get('q100cc') == event2
    assert event_database.get('Q50') == None
    assert 'q100' in event_database


def test_empty_events():
    tef = TEF('./tests/unit_tests/test_datasets/event_file.tef')
    db = tef._event_cf_to_db(tef)
    assert len(db) == 7
