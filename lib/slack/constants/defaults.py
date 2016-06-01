HTK_SLACK_EVENT_TYPE_RESOLVER = 'htk.lib.slack.event_resolvers.default_event_type_resolver'

HTK_SLACK_EVENT_HANDLERS = {
    'default' : 'htk.lib.slack.event_handlers.default',
    'bible' : 'htk.lib.slack.event_handlers.bible',
    'findemail' : 'htk.lib.slack.event_handlers.findemail',
    'help' : 'htk.lib.slack.event_handlers.help',
    'stock' : 'htk.lib.slack.event_handlers.stock',
    'weather' : 'htk.lib.slack.event_handlers.weather',
    'zesty' : 'htk.lib.slack.event_handlers.zesty',
}

HTK_SLACK_EVENT_HANDLERS_EXTRAS = {}

HTK_SLACK_EVENT_HANDLER_USAGES = {
    'help' : 'htk.lib.slack.event_handler_usages.help',
    'default' : 'htk.lib.slack.event_handler_usages.default',
    'bible' : 'htk.lib.slack.event_handler_usages.bible',
    'findemail' : 'htk.lib.slack.event_handler_usages.findemail',
    'stock' : 'htk.lib.slack.event_handler_usages.stock',
    'weather' : 'htk.lib.slack.event_handler_usages.weather',
    'zesty' : 'htk.lib.slack.event_handler_usages.zesty',
}

HTK_SLACK_EVENT_HANDLER_USAGES_EXTRA = {}

# trigger words that are also commands
HTK_SLACK_TRIGGER_COMMAND_WORDS = (
    'bible',
    'findemail',
    'stock',
    'weather',
)

# notifications
HTK_SLACK_NOTIFICATIONS_ENABLED = False

# channels
HTK_SLACK_DEBUG_CHANNEL = '#test'
HTK_SLACK_NOTIFICATIONS_CHANNEL = '#test'
