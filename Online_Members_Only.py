import datetime
from telethon.tl import types as t


def online_within(participant, days):
    status = participant.status
    if isinstance(status, t.UserStatusOnline):
        return True

    last_seen = status.was_online if isinstance(status, t.UserStatusOffline) else None

    if last_seen:
        now = datetime.datetime.now(tz=datetime.timezone.utc)
        diff = now - last_seen
        return diff <= datetime.timedelta(days=days)

    if isinstance(status, t.UserStatusRecently) and days >= 1 \
            or isinstance(status, t.UserStatusLastWeek) and days >= 7 \
            or isinstance(status, t.UserStatusLastMonth) and days >= 30:
        return True

    return False

