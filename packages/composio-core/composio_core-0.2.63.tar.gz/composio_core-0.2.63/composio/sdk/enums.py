from enum import Enum


class Tag(Enum):
    IMPORTANT = ("default", "important")
    ALL = ("default", "all")
    ZOOM_PAC = ("zoom", "PAC")
    ZOOM_REPORTS = ("zoom", "Reports")
    ZOOM_CLOUD_RECORDING = ("zoom", "Cloud Recording")
    ZOOM_TRACKING_FIELD = ("zoom", "Tracking Field")
    ZOOM_H323_DEVICES = ("zoom", "H323 Devices")
    ZOOM_WEBINARS = ("zoom", "Webinars")
    ZOOM_MEETINGS = ("zoom", "Meetings")
    ZOOM_ARCHIVING = ("zoom", "Archiving")
    ZOOM_SIP_PHONE = ("zoom", "SIP Phone")
    ZOOM_DEVICES = ("zoom", "Devices")
    ZOOM_TSP = ("zoom", "TSP")
    LISTENNOTES_SEARCH_API = ("listennotes", "Search API")
    LISTENNOTES_PODCASTER_API = ("listennotes", "Podcaster API")
    LISTENNOTES_DIRECTORY_API = ("listennotes", "Directory API")
    LISTENNOTES_PLAYLIST_API = ("listennotes", "Playlist API")
    LISTENNOTES_INSIGHTS_API = ("listennotes", "Insights API")
    ELEVENLABS_PROJECTS = ("elevenlabs", "projects")
    ELEVENLABS_AUDIO_NATIVE = ("elevenlabs", "audio-native")
    ELEVENLABS_WORKSPACE = ("elevenlabs", "workspace")
    ELEVENLABS_DUBBING = ("elevenlabs", "dubbing")
    ELEVENLABS_VOICES = ("elevenlabs", "voices")
    ELEVENLABS_MODELS = ("elevenlabs", "models")
    ELEVENLABS_SPEECH_HISTORY = ("elevenlabs", "speech-history")
    ELEVENLABS_VOICE_GENERATION = ("elevenlabs", "voice-generation")
    ELEVENLABS_PRONUNCIATION_DICTIONARY = ("elevenlabs", "Pronunciation Dictionary")
    ELEVENLABS_SAMPLES = ("elevenlabs", "samples")
    ELEVENLABS_USER = ("elevenlabs", "user")
    ELEVENLABS_TEXT_TO_SPEECH = ("elevenlabs", "text-to-speech")
    ELEVENLABS_SPEECH_TO_SPEECH = ("elevenlabs", "speech-to-speech")
    BREVO_DOMAINS = ("brevo", "Domains")
    BREVO_CONTACTS = ("brevo", "Contacts")
    BREVO_FILES = ("brevo", "Files")
    BREVO_NOTES = ("brevo", "Notes")
    BREVO_EXTERNAL_FEEDS = ("brevo", "External Feeds")
    BREVO_ACCOUNT = ("brevo", "Account")
    BREVO_WHATSAPP_CAMPAIGNS = ("brevo", "WhatsApp Campaigns")
    BREVO_WEBHOOKS = ("brevo", "Webhooks")
    BREVO_TRANSACTIONAL_WHATSAPP = ("brevo", "Transactional WhatsApp")
    BREVO_RESELLER = ("brevo", "Reseller")
    BREVO_CONVERSATIONS = ("brevo", "Conversations")
    BREVO_DEALS = ("brevo", "Deals")
    BREVO_INBOUND_PARSING = ("brevo", "Inbound Parsing")
    BREVO_EVENT = ("brevo", "Event")
    BREVO_COUPONS = ("brevo", "Coupons")
    BREVO_USER = ("brevo", "User")
    BREVO_TASKS = ("brevo", "Tasks")
    BREVO_TRANSACTIONAL_SMS = ("brevo", "Transactional SMS")
    BREVO_MASTER_ACCOUNT = ("brevo", "Master account")
    BREVO_PROCESS = ("brevo", "Process")
    BREVO_ECOMMERCE = ("brevo", "Ecommerce")
    BREVO_TRANSACTIONAL_EMAILS = ("brevo", "Transactional emails")
    BREVO_SENDERS = ("brevo", "Senders")
    BREVO_COMPANIES = ("brevo", "Companies")
    BREVO_EMAIL_CAMPAIGNS = ("brevo", "Email Campaigns")
    BREVO_SMS_CAMPAIGNS = ("brevo", "SMS Campaigns")
    ATTIO_META = ("attio", "Meta")
    ATTIO_ENTRIES = ("attio", "Entries")
    ATTIO_WORKSPACE_MEMBERS = ("attio", "Workspace members")
    ATTIO_ATTRIBUTES = ("attio", "Attributes")
    ATTIO_NOTES = ("attio", "Notes")
    ATTIO_RECORDS = ("attio", "Records")
    ATTIO_LISTS = ("attio", "Lists")
    ATTIO_THREADS = ("attio", "Threads")
    ATTIO_OBJECTS = ("attio", "Objects")
    ATTIO_WEBHOOKS = ("attio", "Webhooks")
    ATTIO_COMMENTS = ("attio", "Comments")
    ATTIO_TASKS = ("attio", "Tasks")
    ASANA_WORKSPACES = ("asana", "Workspaces")
    ASANA_PROJECT_STATUSES = ("asana", "Project statuses")
    ASANA_CUSTOM_FIELDS = ("asana", "Custom fields")
    ASANA_USERS = ("asana", "Users")
    ASANA_PORTFOLIOS = ("asana", "Portfolios")
    ASANA_PROJECT_BRIEFS = ("asana", "Project briefs")
    ASANA_TEAM_MEMBERSHIPS = ("asana", "Team memberships")
    ASANA_JOBS = ("asana", "Jobs")
    ASANA_AUDIT_LOG_API = ("asana", "Audit log API")
    ASANA_RULES = ("asana", "Rules")
    ASANA_PROJECTS = ("asana", "Projects")
    ASANA_TEAMS = ("asana", "Teams")
    ASANA_STORIES = ("asana", "Stories")
    ASANA_ALLOCATIONS = ("asana", "Allocations")
    ASANA_ORGANIZATION_EXPORTS = ("asana", "Organization exports")
    ASANA_WEBHOOKS = ("asana", "Webhooks")
    ASANA_PORTFOLIO_MEMBERSHIPS = ("asana", "Portfolio memberships")
    ASANA_SECTIONS = ("asana", "Sections")
    ASANA_MEMBERSHIPS = ("asana", "Memberships")
    ASANA_TYPEAHEAD = ("asana", "Typeahead")
    ASANA_ATTACHMENTS = ("asana", "Attachments")
    ASANA_PROJECT_MEMBERSHIPS = ("asana", "Project memberships")
    ASANA_TIME_TRACKING_ENTRIES = ("asana", "Time tracking entries")
    ASANA_STATUS_UPDATES = ("asana", "Status updates")
    ASANA_CUSTOM_FIELD_SETTINGS = ("asana", "Custom field settings")
    ASANA_WORKSPACE_MEMBERSHIPS = ("asana", "Workspace memberships")
    ASANA_TIME_PERIODS = ("asana", "Time periods")
    ASANA_GOALS = ("asana", "Goals")
    ASANA_TASKS = ("asana", "Tasks")
    ASANA_TASK_TEMPLATES = ("asana", "Task templates")
    ASANA_EVENTS = ("asana", "Events")
    ASANA_BATCH_API = ("asana", "Batch API")
    ASANA_USER_TASK_LISTS = ("asana", "User task lists")
    ASANA_PROJECT_TEMPLATES = ("asana", "Project templates")
    ASANA_GOAL_RELATIONSHIPS = ("asana", "Goal relationships")
    ASANA_TAGS = ("asana", "Tags")
    OKTA_FEATURE = ("okta", "Feature")
    OKTA_GROUP = ("okta", "Group")
    OKTA_PROFILEMAPPING = ("okta", "ProfileMapping")
    OKTA_LINKEDOBJECT = ("okta", "LinkedObject")
    OKTA_THREATINSIGHT = ("okta", "ThreatInsight")
    OKTA_IDENTITYPROVIDER = ("okta", "IdentityProvider")
    OKTA_AUTHORIZATIONSERVER = ("okta", "AuthorizationServer")
    OKTA_INLINEHOOK = ("okta", "InlineHook")
    OKTA_TEMPLATE = ("okta", "Template")
    OKTA_AUTHENTICATOR = ("okta", "Authenticator")
    OKTA_SUBSCRIPTION = ("okta", "Subscription")
    OKTA_USERFACTOR = ("okta", "UserFactor")
    OKTA_POLICY = ("okta", "Policy")
    OKTA_GROUPSCHEMA = ("okta", "GroupSchema")
    OKTA_DOMAIN = ("okta", "Domain")
    OKTA_LOG = ("okta", "Log")
    OKTA_ORG = ("okta", "Org")
    OKTA_BRAND = ("okta", "Brand")
    OKTA_TRUSTEDORIGIN = ("okta", "TrustedOrigin")
    OKTA_USER = ("okta", "User")
    OKTA_SESSION = ("okta", "Session")
    OKTA_APPLICATION = ("okta", "Application")
    OKTA_USERTYPE = ("okta", "UserType")
    OKTA_NETWORKZONE = ("okta", "NetworkZone")
    OKTA_USERSCHEMA = ("okta", "UserSchema")
    OKTA_EVENTHOOK = ("okta", "EventHook")


class App(Enum):
    YNAB = "ynab"
    YOUTUBE = "youtube"
    ZENDESK = "zendesk"
    ZENSERP = "zenserp"
    ZOHO = "zoho"
    EXA = "exa"
    FILEMANAGER = "filemanager"
    SCHEDULER = "scheduler"
    ZOOM = "zoom"
    LISTENNOTES = "listennotes"
    ELEVENLABS = "elevenlabs"
    BREVO = "brevo"
    ATTIO = "attio"
    BOLDSIGN = "boldsign"
    MICROSOFT_TENANT_SPECIFIC = "microsoft-tenant-specific"
    FITBIT = "fitbit"
    RAVEN_SEO_TOOLS = "raven seo tools"
    WABOXAPP = "waboxapp"
    CHATWORK = "chatwork"
    TAPFORM = "tapform"
    BEEMINDER = "beeminder"
    ABLY = "ably"
    SIMPLESAT = "simplesat"
    ACTIVECAMPAIGN = "activecampaign"
    INTERCOM = "intercom"
    ZOHO_BOOKS = "zoho books"
    RINGCENTRAL = "ringcentral"
    PRODUCTBOARD = "productboard"
    SMART_RECRUITERS = "smart recruiters"
    AERO_WORKFLOW = "aero-workflow"
    HARVEST = "harvest"
    ACCELO = "accelo"
    STACK_EXCHANGE = "stack exchange"
    PROCESS_STREET = "process street"
    FRESHDESK = "freshdesk"
    HIGHLEVEL = "highlevel"
    BATTLE_NET = "battle.net"
    BREX = "brex"
    LEVER = "lever"
    BRAINTREE = "braintree"
    FRESHBOOKS = "freshbooks"
    CALENDLY = "calendly"
    SMUGMUG = "smugmug"
    BLACKBAUD = "blackbaud"
    ZOHO_DESK = "zoho desk"
    CLOUDFLARE = "cloudflare"
    HACKERRANK_WORK = "hackerrank-work"
    HUMANLOOP = "humanloop"
    WAKATIME = "wakatime"
    GUMROAD = "gumroad"
    GITLAB = "gitlab"
    SHOPIFY = "shopify"
    PLACEKEY = "placekey"
    CONTENTFUL = "contentful"
    FACTORIAL = "factorial"
    SERVICEM8 = "servicem8"
    DEMIO = "demio"
    PANDADOC = "pandadoc"
    WEBFLOW = "webflow"
    FRONT = "front"
    ECHTPOST = "echtpost"
    ATLASSIAN = "atlassian"
    MAINTAINX = "maintainx"
    ZOHO_MAIL = "zoho mail"
    DISCORD = "discord"
    BROWSERHUB = "browserhub"
    WORKABLE = "workable"
    HUBSPOT = "hubspot"
    FACEBOOK = "facebook"
    HELCIM = "helcim"
    ALTOVIZ = "altoviz"
    ZOHO_INVOICE = "zoho invoice"
    BITWARDEN = "bitwarden"
    MONDAY = "monday"
    EVENTBRITE = "eventbrite"
    SHORTCUT = "shortcut"
    ONE_DRIVE = "one-drive"
    ADOBE = "adobe"
    INTERZOID = "interzoid"
    SALESFORCE = "salesforce"
    CUSTOMER_IO = "customer.io"
    RAFFLYS = "rafflys"
    STRAVA = "strava"
    MBOUM = "mboum"
    TISANE_AI = "tisane.ai"
    DAILYBOT = "dailybot"
    NGROK = "ngrok"
    WAVE_ACCOUNTING = "wave accounting"
    XERO = "xero"
    LEXOFFICE = "lexoffice"
    MOXIE = "moxie"
    LASTPASS = "lastpass"
    FINAGE = "finage"
    SQUARE = "square"
    YANDEX = "yandex"
    REDDIT = "reddit"
    HEROKU = "heroku"
    BRANDFETCH = "brandfetch"
    QUALAROO = "qualaroo"
    PRINTNODE = "printnode"
    FORMCARRY = "formcarry"
    MIRO = "miro"
    TERMINUS = "terminus"
    PAGERDUTY = "pagerduty"
    PIPEDRIVE = "pipedrive"
    BASEROW_API = "baserow api"
    DATAGMA = "datagma"
    MICROSOFT_TEAMS = "microsoft-teams"
    BROWSE_AI = "browse.ai"
    KLAVIYO = "klaviyo"
    TIMEKIT = "timekit"
    BREX_STAGING = "brex-staging"
    FLUTTERWAVE = "flutterwave"
    BANNERBEAR = "bannerbear"
    DOCMOSIS = "docmosis"
    VERO = "vero"
    DROPBOX_SIGN = "dropbox sign"
    DIGICERT = "digicert"
    UNNAMED_TOOL = "unnamed tool"
    TINYURL = "tinyurl"
    TASKADE = "taskade"
    DATADOG = "datadog"
    LINKHUT = "linkhut"
    AUTH0 = "auth0"
    KEAP = "keap"
    FIGMA = "figma"
    APPDRAG = "appdrag"
    EXIST = "exist"
    COINMARKETCAL = "coinmarketcal"
    AXONAUT = "axonaut"
    FORMSITE = "formsite"
    TODOIST = "todoist"
    MOCEAN_API = "mocean api"
    SURVEY_MONKEY = "survey monkey"
    ZOHO_INVENTORY = "zoho inventory"
    CLOSE = "close"
    ROCKETREACH = "rocketreach"
    TINYPNG = "tinypng"
    ALCHEMY = "alchemy"
    FOMO = "fomo"
    MIXPANEL = "mixpanel"
    BOX = "box"
    SPOTIFY = "spotify"
    GORGIAS = "gorgias"
    TWITTER = "twitter"
    TWITCH = "twitch"
    MORE_TREES = "more trees"
    KLIPFOLIO = "klipfolio"
    NETSUITE = "netsuite"
    WORKIOM = "workiom"
    AMCARDS = "amcards"
    AMPLITUDE = "amplitude"
    BOTBABA = "botbaba"
    NCSCALE = "ncscale"
    LAUNCHDARKLY = "launchdarkly"
    SCREENSHOTONE = "screenshotone"
    BAMBOOHR = "bamboohr"
    GURU = "guru"
    EPIC_GAMES = "epic-games"
    JIRA = "jira"
    ASHBY = "ashby"
    DEEL = "deel"
    CAL_COM = "cal.com"
    BUBBLE = "bubble"
    ONCEHUB = "oncehub"
    ZOHO_BIGIN = "zoho bigin"
    TIMELY = "timely"
    TONEDEN = "toneden"
    METATEXTAI = "metatextai"
    MAILCHIMP = "mailchimp"
    AMAZON = "amazon"
    VENLY = "venly"
    SAGE = "sage"
    TEXTRAZOR = "textrazor"
    MURAL = "mural"
    CHMEETINGS = "chmeetings"
    GITHUB = "github"
    LINEAR = "linear"
    ASANA = "asana"
    TRELLO = "trello"
    NOTION = "notion"
    TYPEFORM = "typeform"
    DROPBOX = "dropbox"
    SLACK = "slack"
    APIFY = "apify"
    GOOGLECALENDAR = "googlecalendar"
    GMAIL = "gmail"
    SLACKBOT = "slackbot"
    CODEINTERPRETER = "codeinterpreter"
    SERPAPI = "serpapi"
    SNOWFLAKE = "snowflake"
    OKTA = "okta"
    TEST_ASANA = "test_asana"


class Action(Enum):
    def __init__(self, service, action, no_auth):
        self.service = service
        self.action = action
        self.no_auth = no_auth

    ZENDESK_CREATE_ZENDESK_ORGANIZATION = (
        "zendesk",
        "zendesk_create_zendesk_organization",
        False,
    )
    ZENDESK_DELETE_ZENDESK_ORGANIZATION = (
        "zendesk",
        "zendesk_delete_zendesk_organization",
        False,
    )
    ZENDESK_COUNT_ZENDESK_ORGANIZATIONS = (
        "zendesk",
        "zendesk_count_zendesk_organizations",
        False,
    )
    ZENDESK_GET_ZENDESK_ORGANIZATION = (
        "zendesk",
        "zendesk_get_zendesk_organization",
        False,
    )
    ZENDESK_GET_ALL_ZENDESK_ORGANIZATIONS = (
        "zendesk",
        "zendesk_get_all_zendesk_organizations",
        False,
    )
    ZENDESK_UPDATE_ZENDESK_ORGANIZATION = (
        "zendesk",
        "zendesk_update_zendesk_organization",
        False,
    )
    ZENDESK_CREATE_ZENDESK_TICKET = ("zendesk", "zendesk_create_zendesk_ticket", False)
    ZENDESK_DELETE_ZENDESK_TICKET = ("zendesk", "zendesk_delete_zendesk_ticket", False)
    ZENDESK_GET_ABOUT_ME = ("zendesk", "zendesk_get_about_me", False)
    EXA_SEARCH = ("exa", "exa_search", True)
    EXA_SIMILARLINK = ("exa", "exa_similarlink", True)
    FILEMANAGER_CREATE_SHELL_ACTION = (
        "filemanager",
        "filemanager_create_shell_action",
        True,
    )
    FILEMANAGER_CLOSE_SHELL_ACTION = (
        "filemanager",
        "filemanager_close_shell_action",
        True,
    )
    FILEMANAGER_RUN_COMMAND_ACTION = (
        "filemanager",
        "filemanager_run_command_action",
        True,
    )
    FILEMANAGER_SET_ENV_VAR_ACTION = (
        "filemanager",
        "filemanager_set_env_var_action",
        True,
    )
    FILEMANAGER_OPEN_FILE_ACTION = ("filemanager", "filemanager_open_file_action", True)
    FILEMANAGER_GOTO_LINE_ACTION = ("filemanager", "filemanager_goto_line_action", True)
    FILEMANAGER_SCROLL_ACTION = ("filemanager", "filemanager_scroll_action", True)
    FILEMANAGER_CREATE_FILE_ACTION = (
        "filemanager",
        "filemanager_create_file_action",
        True,
    )
    FILEMANAGER_EDIT_FILE_ACTION = ("filemanager", "filemanager_edit_file_action", True)
    SCHEDULER_SCHEDULE_JOB_ACTION = ("scheduler", "scheduler_schedule_job_action", True)
    ZOOM_ARCHIVING_MEETING_FILES_LIST = (
        "zoom",
        "zoom_archiving_meeting_files_list",
        False,
    )
    ZOOM_ARCHIVING_GET_STATISTICS = ("zoom", "zoom_archiving_get_statistics", False)
    ZOOM_ARCHIVING_UPDATE_AUTO_DELETE_STATUS = (
        "zoom",
        "zoom_archiving_update_auto_delete_status",
        False,
    )
    ZOOM_ARCHIVING_MEETING_FILES_LIST2 = (
        "zoom",
        "zoom_archiving_meeting_files_list2",
        False,
    )
    ZOOM_ARCHIVING_MEETING_FILES_DELETE = (
        "zoom",
        "zoom_archiving_meeting_files_delete",
        False,
    )
    ZOOM_CLOUD_RECORDING_GET_MEETING_RECORDINGS = (
        "zoom",
        "zoom_cloud_recording_get_meeting_recordings",
        False,
    )
    ZOOM_CLOUD_RECORDING_DELETE_MEETING_RECORDINGS = (
        "zoom",
        "zoom_cloud_recording_delete_meeting_recordings",
        False,
    )
    ZOOM_ANALYTICS_DETAILS = ("zoom", "zoom_analytics_details", False)
    ZOOM_ANALYTICS_SUMMARY = ("zoom", "zoom_analytics_summary", False)
    ZOOM_CLOUD_RECORDING_LIST_REGISTRANTS = (
        "zoom",
        "zoom_cloud_recording_list_registrants",
        False,
    )
    ZOOM_CLOUD_RECORDING_CREATE_REGISTRANT = (
        "zoom",
        "zoom_cloud_recording_create_registrant",
        False,
    )
    ZOOM_CLOUD_RECORDING_LIST_REGISTRATION_QUESTIONS = (
        "zoom",
        "zoom_cloud_recording_list_registration_questions",
        False,
    )
    ZOOM_CLOUD_RECORDING_UPDATE_REGISTRATION_QUESTIONS = (
        "zoom",
        "zoom_cloud_recording_update_registration_questions",
        False,
    )
    ZOOM_CLOUD_RECORDING_UPDATE_REGISTRANT_STATUS = (
        "zoom",
        "zoom_cloud_recording_update_registrant_status",
        False,
    )
    ZOOM_CLOUD_RECORDING_GET_SETTINGS = (
        "zoom",
        "zoom_cloud_recording_get_settings",
        False,
    )
    ZOOM_CLOUD_RECORDING_UPDATE_SETTINGS = (
        "zoom",
        "zoom_cloud_recording_update_settings",
        False,
    )
    ZOOM_CLOUD_RECORDING_DELETE_RECORDING = (
        "zoom",
        "zoom_cloud_recording_delete_recording",
        False,
    )
    ZOOM_CLOUD_RECORDING_RECOVER_STATUS = (
        "zoom",
        "zoom_cloud_recording_recover_status",
        False,
    )
    ZOOM_CLOUD_RECORDING_RECOVER_RECORDING_STATUS = (
        "zoom",
        "zoom_cloud_recording_recover_recording_status",
        False,
    )
    ZOOM_CLOUD_RECORDING_LIST_RECORDINGS = (
        "zoom",
        "zoom_cloud_recording_list_recordings",
        False,
    )
    ZOOM_DEVICES_LIST = ("zoom", "zoom_devices_list", False)
    ZOOM_DEVICES_CREATE_NEW_DEVICE = ("zoom", "zoom_devices_create_new_device", False)
    ZOOM_DEVICES_LIST_ZDM_GROUP_INFO = (
        "zoom",
        "zoom_devices_list_zdm_group_info",
        False,
    )
    ZOOM_DEVICES_ASSIGN_DEVICE_ZPA_ASSIGNMENT = (
        "zoom",
        "zoom_devices_assign_device_zpa_assignment",
        False,
    )
    ZOOM_DEVICES_UPGRADE_ZPA_OS_APP = ("zoom", "zoom_devices_upgrade_zpa_os_app", False)
    ZOOM_DEVICES_REMOVE_ZPA_DEVICE_BY_VENDOR_AND_MAC_ADDRESS = (
        "zoom",
        "zoom_devices_remove_zpa_device_by_vendor_and_mac_address",
        False,
    )
    ZOOM_DEVICES_GET_ZPA_VERSION_INFO = (
        "zoom",
        "zoom_devices_get_zpa_version_info",
        False,
    )
    ZOOM_DEVICES_GET_DETAIL = ("zoom", "zoom_devices_get_detail", False)
    ZOOM_DEVICES_REMOVE_DEVICE_ZMD = ("zoom", "zoom_devices_remove_device_zmd", False)
    ZOOM_DEVICES_UPDATE_DEVICE_NAME = ("zoom", "zoom_devices_update_device_name", False)
    ZOOM_DEVICES_CHANGE_DEVICE_ASSOCIATION = (
        "zoom",
        "zoom_devices_change_device_association",
        False,
    )
    ZOOM_H323_DEVICES_LIST_DEVICES = ("zoom", "zoom_h323_devices_list_devices", False)
    ZOOM_H323_DEVICES_CREATE_DEVICE = ("zoom", "zoom_h323_devices_create_device", False)
    ZOOM_H323_DEVICES_DELETE_DEVICE = ("zoom", "zoom_h323_devices_delete_device", False)
    ZOOM_H323_DEVICES_UPDATE_DEVICE_INFO = (
        "zoom",
        "zoom_h323_devices_update_device_info",
        False,
    )
    ZOOM_MEETINGS_DELETE_MEETING_CHAT_MESSAGE = (
        "zoom",
        "zoom_meetings_delete_meeting_chat_message",
        False,
    )
    ZOOM_MEETINGS_UPDATE_MESSAGE = ("zoom", "zoom_meetings_update_message", False)
    ZOOM_MEETINGS_CONTROL_IN_MEETING_FEATURES = (
        "zoom",
        "zoom_meetings_control_in_meeting_features",
        False,
    )
    ZOOM_MEETINGS_LIST_MEETING_SUMMARIES = (
        "zoom",
        "zoom_meetings_list_meeting_summaries",
        False,
    )
    ZOOM_MEETINGS_GET_DETAILS = ("zoom", "zoom_meetings_get_details", False)
    ZOOM_MEETINGS_REMOVE_MEETING = ("zoom", "zoom_meetings_remove_meeting", False)
    ZOOM_MEETINGS_UPDATE_DETAILS = ("zoom", "zoom_meetings_update_details", False)
    ZOOM_MEETINGS_CREATE_BATCH_POLLS = (
        "zoom",
        "zoom_meetings_create_batch_polls",
        False,
    )
    ZOOM_MEETINGS_BATCH_REGISTRANTS_CREATE = (
        "zoom",
        "zoom_meetings_batch_registrants_create",
        False,
    )
    ZOOM_MEETINGS_GET_INVITATION_NOTE = (
        "zoom",
        "zoom_meetings_get_invitation_note",
        False,
    )
    ZOOM_MEETINGS_CREATE_INVITE_LINKS = (
        "zoom",
        "zoom_meetings_create_invite_links",
        False,
    )
    ZOOM_MEETINGS_GET_JOIN_TOKEN = ("zoom", "zoom_meetings_get_join_token", False)
    ZOOM_MEETINGS_GET_MEETING_ARCHIVE_TOKEN_FOR_LOCAL_ARCHIVING = (
        "zoom",
        "zoom_meetings_get_meeting_archive_token_for_local_archiving",
        False,
    )
    ZOOM_MEETINGS_GET_JOIN_TOKEN_LOCAL_RECORDING = (
        "zoom",
        "zoom_meetings_get_join_token_local_recording",
        False,
    )
    ZOOM_MEETINGS_GET_LIVE_STREAM_DETAILS = (
        "zoom",
        "zoom_meetings_get_live_stream_details",
        False,
    )
    ZOOM_MEETINGS_UPDATE_LIVE_STREAM = (
        "zoom",
        "zoom_meetings_update_live_stream",
        False,
    )
    ZOOM_MEETINGS_LIVE_STREAM_STATUS_UPDATE = (
        "zoom",
        "zoom_meetings_live_stream_status_update",
        False,
    )
    ZOOM_MEETINGS_GET_MEETING_SUMMARY = (
        "zoom",
        "zoom_meetings_get_meeting_summary",
        False,
    )
    ZOOM_MEETINGS_LIST_MEETING_POLLS = (
        "zoom",
        "zoom_meetings_list_meeting_polls",
        False,
    )
    ZOOM_MEETINGS_CREATE_POLL = ("zoom", "zoom_meetings_create_poll", False)
    ZOOM_MEETINGS_GET_POLL = ("zoom", "zoom_meetings_get_poll", False)
    ZOOM_MEETINGS_UPDATE_MEETING_POLL = (
        "zoom",
        "zoom_meetings_update_meeting_poll",
        False,
    )
    ZOOM_MEETINGS_POLL_DELETE = ("zoom", "zoom_meetings_poll_delete", False)
    ZOOM_MEETINGS_LIST_REGISTRANTS = ("zoom", "zoom_meetings_list_registrants", False)
    ZOOM_MEETINGS_ADD_REGISTRANT = ("zoom", "zoom_meetings_add_registrant", False)
    ZOOM_MEETINGS_LIST_REGISTRATION_QUESTIONS = (
        "zoom",
        "zoom_meetings_list_registration_questions",
        False,
    )
    ZOOM_MEETINGS_UPDATE_REGISTRATION_QUESTIONS = (
        "zoom",
        "zoom_meetings_update_registration_questions",
        False,
    )
    ZOOM_MEETINGS_UPDATE_REGISTRANT_STATUS = (
        "zoom",
        "zoom_meetings_update_registrant_status",
        False,
    )
    ZOOM_MEETINGS_GET_REGISTRANT_DETAILS = (
        "zoom",
        "zoom_meetings_get_registrant_details",
        False,
    )
    ZOOM_MEETINGS_DELETE_REGISTRANT = ("zoom", "zoom_meetings_delete_registrant", False)
    ZOOM_MEETINGS_GETS_IP_URI_WITH_PASS_CODE = (
        "zoom",
        "zoom_meetings_gets_ip_uri_with_pass_code",
        False,
    )
    ZOOM_MEETINGS_UPDATE_MEETING_STATUS = (
        "zoom",
        "zoom_meetings_update_meeting_status",
        False,
    )
    ZOOM_MEETINGS_GET_MEETING_SURVEY = (
        "zoom",
        "zoom_meetings_get_meeting_survey",
        False,
    )
    ZOOM_MEETINGS_DELETE_MEETING_SURVEY = (
        "zoom",
        "zoom_meetings_delete_meeting_survey",
        False,
    )
    ZOOM_MEETINGS_UPDATE_SURVEY = ("zoom", "zoom_meetings_update_survey", False)
    ZOOM_MEETINGS_GET_MEETING_TOKEN = ("zoom", "zoom_meetings_get_meeting_token", False)
    ZOOM_MEETINGS_GET_DETAILS2 = ("zoom", "zoom_meetings_get_details2", False)
    ZOOM_MEETINGS_LIST_PAST_MEETING_INSTANCES = (
        "zoom",
        "zoom_meetings_list_past_meeting_instances",
        False,
    )
    ZOOM_MEETINGS_GET_PAST_MEETING_PARTICIPANTS = (
        "zoom",
        "zoom_meetings_get_past_meeting_participants",
        False,
    )
    ZOOM_MEETINGS_LIST_PAST_MEETING_POLLS = (
        "zoom",
        "zoom_meetings_list_past_meeting_polls",
        False,
    )
    ZOOM_MEETINGS_LIST_PAST_MEETING_QA = (
        "zoom",
        "zoom_meetings_list_past_meeting_qa",
        False,
    )
    ZOOM_MEETINGS_LIST_MEETING_TEMPLATES = (
        "zoom",
        "zoom_meetings_list_meeting_templates",
        False,
    )
    ZOOM_MEETINGS_CREATE_TEMPLATE_FROM_MEETING = (
        "zoom",
        "zoom_meetings_create_template_from_meeting",
        False,
    )
    ZOOM_MEETINGS_LIST_HOST_SCHEDULED = (
        "zoom",
        "zoom_meetings_list_host_scheduled",
        False,
    )
    ZOOM_MEETINGS_CREATE_MEETING = ("zoom", "zoom_meetings_create_meeting", False)
    ZOOM_MEETINGS_LIST_UPCOMING_MEETINGS = (
        "zoom",
        "zoom_meetings_list_upcoming_meetings",
        False,
    )
    ZOOM_PAC_LIST_ACCOUNTS = ("zoom", "zoom_pac_list_accounts", False)
    ZOOM_REPORTS_LIST_SIGN_IN_SIGN_OUT_ACTIVITIES = (
        "zoom",
        "zoom_reports_list_sign_in_sign_out_activities",
        False,
    )
    ZOOM_REPORTS_GET_BILLING_DEPARTMENT_REPORTS = (
        "zoom",
        "zoom_reports_get_billing_department_reports",
        False,
    )
    ZOOM_REPORTS_GET_BILLING_INVOICES = (
        "zoom",
        "zoom_reports_get_billing_invoices",
        False,
    )
    ZOOM_REPORTS_GET_CLOUD_RECORDING_USAGE_REPORT = (
        "zoom",
        "zoom_reports_get_cloud_recording_usage_report",
        False,
    )
    ZOOM_REPORTS_GET_DAILY_USAGE_REPORT = (
        "zoom",
        "zoom_reports_get_daily_usage_report",
        False,
    )
    ZOOM_REPORTS_GET_MEETING_DETAIL_REPORTS = (
        "zoom",
        "zoom_reports_get_meeting_detail_reports",
        False,
    )
    ZOOM_REPORTS_GET_MEETING_PARTICIPANT_REPORTS = (
        "zoom",
        "zoom_reports_get_meeting_participant_reports",
        False,
    )
    ZOOM_REPORTS_GET_MEETING_POLL_REPORTS = (
        "zoom",
        "zoom_reports_get_meeting_poll_reports",
        False,
    )
    ZOOM_REPORTS_GET_MEETING_QA_REPORT = (
        "zoom",
        "zoom_reports_get_meeting_qa_report",
        False,
    )
    ZOOM_REPORTS_GET_MEETING_SURVEY_REPORT = (
        "zoom",
        "zoom_reports_get_meeting_survey_report",
        False,
    )
    ZOOM_REPORTS_GET_OPERATION_LOGS_REPORT = (
        "zoom",
        "zoom_reports_get_operation_logs_report",
        False,
    )
    ZOOM_REPORTS_GET_TELEPHONE_REPORTS = (
        "zoom",
        "zoom_reports_get_telephone_reports",
        False,
    )
    ZOOM_REPORTS_LIST_UPCOMING_EVENTS_REPORT = (
        "zoom",
        "zoom_reports_list_upcoming_events_report",
        False,
    )
    ZOOM_REPORTS_GET_ACTIVE_INACTIVE_HOST_REPORTS = (
        "zoom",
        "zoom_reports_get_active_inactive_host_reports",
        False,
    )
    ZOOM_REPORTS_GET_MEETING_REPORTS = (
        "zoom",
        "zoom_reports_get_meeting_reports",
        False,
    )
    ZOOM_REPORTS_GET_WEB_IN_AR_DETAILS_REPORT = (
        "zoom",
        "zoom_reports_get_web_in_ar_details_report",
        False,
    )
    ZOOM_REPORTS_WEB_IN_AR_PARTICIPANTS_LIST = (
        "zoom",
        "zoom_reports_web_in_ar_participants_list",
        False,
    )
    ZOOM_REPORTS_GET_WEB_IN_AR_POLL_REPORTS = (
        "zoom",
        "zoom_reports_get_web_in_ar_poll_reports",
        False,
    )
    ZOOM_REPORTS_GET_WEB_IN_AR_QA_REPORT = (
        "zoom",
        "zoom_reports_get_web_in_ar_qa_report",
        False,
    )
    ZOOM_REPORTS_GET_WEB_IN_AR_SURVEY_REPORT = (
        "zoom",
        "zoom_reports_get_web_in_ar_survey_report",
        False,
    )
    ZOOM_SIP_PHONE_LIST = ("zoom", "zoom_sip_phone_list", False)
    ZOOM_SIP_PHONE_ENABLE_USERS_IP_PHONE = (
        "zoom",
        "zoom_sip_phone_enable_users_ip_phone",
        False,
    )
    ZOOM_SIP_PHONE_DELETE_PHONE = ("zoom", "zoom_sip_phone_delete_phone", False)
    ZOOM_SIP_PHONE_UPDATE_SPECIFIC_PHONE = (
        "zoom",
        "zoom_sip_phone_update_specific_phone",
        False,
    )
    ZOOM_TSP_GET_ACCOUNT_INFO = ("zoom", "zoom_tsp_get_account_info", False)
    ZOOM_TSP_UPDATE_ACCOUNT_TSP_INFORMATION = (
        "zoom",
        "zoom_tsp_update_account_tsp_information",
        False,
    )
    ZOOM_TSP_LIST_USE_RTSP_ACCOUNTS = ("zoom", "zoom_tsp_list_use_rtsp_accounts", False)
    ZOOM_TSP_ADD_USE_RTSP_ACCOUNT = ("zoom", "zoom_tsp_add_use_rtsp_account", False)
    ZOOM_TSP_SET_GLOBAL_DIAL_IN_URL = ("zoom", "zoom_tsp_set_global_dial_in_url", False)
    ZOOM_TSP_GET_USE_RTSP_ACCOUNT = ("zoom", "zoom_tsp_get_use_rtsp_account", False)
    ZOOM_TSP_DELETE_USE_RTSP_ACCOUNT = (
        "zoom",
        "zoom_tsp_delete_use_rtsp_account",
        False,
    )
    ZOOM_TSP_UPDATE_USE_RTSP_ACCOUNT = (
        "zoom",
        "zoom_tsp_update_use_rtsp_account",
        False,
    )
    ZOOM_TRACKING_FIELD_LIST = ("zoom", "zoom_tracking_field_list", False)
    ZOOM_TRACKING_FIELD_CREATE_FIELD = (
        "zoom",
        "zoom_tracking_field_create_field",
        False,
    )
    ZOOM_TRACKING_FIELD_GET = ("zoom", "zoom_tracking_field_get", False)
    ZOOM_TRACKING_FIELD_DELETE_FIELD = (
        "zoom",
        "zoom_tracking_field_delete_field",
        False,
    )
    ZOOM_TRACKING_FIELD_UPDATE = ("zoom", "zoom_tracking_field_update", False)
    ZOOM_WEB_IN_ARS_DELETE_MESSAGE_BY_ID = (
        "zoom",
        "zoom_web_in_ars_delete_message_by_id",
        False,
    )
    ZOOM_WEB_IN_ARS_LIST_ABSENTEES = ("zoom", "zoom_web_in_ars_list_absentees", False)
    ZOOM_WEB_IN_ARS_LIST_PAST_INSTANCES = (
        "zoom",
        "zoom_web_in_ars_list_past_instances",
        False,
    )
    ZOOM_WEB_IN_ARS_LIST_PARTICIPANTS = (
        "zoom",
        "zoom_web_in_ars_list_participants",
        False,
    )
    ZOOM_WEB_IN_ARS_LIST_POLL_RESULTS = (
        "zoom",
        "zoom_web_in_ars_list_poll_results",
        False,
    )
    ZOOM_WEB_IN_ARS_LIST_PAST_WEB_IN_AR_QA = (
        "zoom",
        "zoom_web_in_ars_list_past_web_in_ar_qa",
        False,
    )
    ZOOM_WEB_IN_ARS_LIST_WEB_IN_AR_TEMPLATES = (
        "zoom",
        "zoom_web_in_ars_list_web_in_ar_templates",
        False,
    )
    ZOOM_WEB_IN_ARS_CREATE_WEB_IN_AR_TEMPLATE = (
        "zoom",
        "zoom_web_in_ars_create_web_in_ar_template",
        False,
    )
    ZOOM_WEB_IN_ARS_LIST_WEB_IN_ARS = ("zoom", "zoom_web_in_ars_list_web_in_ars", False)
    ZOOM_WEB_IN_ARS_CREATE_WEB_IN_AR = (
        "zoom",
        "zoom_web_in_ars_create_web_in_ar",
        False,
    )
    ZOOM_WEB_IN_ARS_GET_DETAILS = ("zoom", "zoom_web_in_ars_get_details", False)
    ZOOM_WEB_IN_ARS_REMOVE_WEB_IN_AR = (
        "zoom",
        "zoom_web_in_ars_remove_web_in_ar",
        False,
    )
    ZOOM_WEB_IN_ARS_UPDATE_SCHEDULED_WEB_IN_AR = (
        "zoom",
        "zoom_web_in_ars_update_scheduled_web_in_ar",
        False,
    )
    ZOOM_WEB_IN_ARS_CREATE_BATCH_REGISTRANTS = (
        "zoom",
        "zoom_web_in_ars_create_batch_registrants",
        False,
    )
    ZOOM_WEB_IN_ARS_GET_SESSION_BRANDING = (
        "zoom",
        "zoom_web_in_ars_get_session_branding",
        False,
    )
    ZOOM_WEB_IN_ARS_CREATE_BRANDING_NAME_TAG = (
        "zoom",
        "zoom_web_in_ars_create_branding_name_tag",
        False,
    )
    ZOOM_WEB_IN_ARS_DELETE_BRANDING_NAME_TAG = (
        "zoom",
        "zoom_web_in_ars_delete_branding_name_tag",
        False,
    )
    ZOOM_WEB_IN_ARS_UPDATE_BRANDING_NAME_TAG = (
        "zoom",
        "zoom_web_in_ars_update_branding_name_tag",
        False,
    )
    ZOOM_WEB_IN_ARS_UPLOAD_BRANDING_VIRTUAL_BACKGROUND = (
        "zoom",
        "zoom_web_in_ars_upload_branding_virtual_background",
        False,
    )
    ZOOM_WEB_IN_ARS_DELETE_BRANDING_VIRTUAL_BACKGROUND = (
        "zoom",
        "zoom_web_in_ars_delete_branding_virtual_background",
        False,
    )
    ZOOM_WEB_IN_ARS_SET_DEFAULT_BRANDING_VIRTUAL_BACKGROUND = (
        "zoom",
        "zoom_web_in_ars_set_default_branding_virtual_background",
        False,
    )
    ZOOM_WEB_IN_ARS_UPLOAD_BRANDING_WALLPAPER = (
        "zoom",
        "zoom_web_in_ars_upload_branding_wallpaper",
        False,
    )
    ZOOM_WEB_IN_ARS_DELETE_BRANDING_WALLPAPER = (
        "zoom",
        "zoom_web_in_ars_delete_branding_wallpaper",
        False,
    )
    ZOOM_WEB_IN_ARS_CREATE_INVITE_LINKS = (
        "zoom",
        "zoom_web_in_ars_create_invite_links",
        False,
    )
    ZOOM_WEB_IN_ARS_JOIN_TOKEN_LIVE_STREAMING = (
        "zoom",
        "zoom_web_in_ars_join_token_live_streaming",
        False,
    )
    ZOOM_WEB_IN_ARS_GET_MEETING_ARCHIVE_TOKEN_FOR_LOCAL_ARCHIVING = (
        "zoom",
        "zoom_web_in_ars_get_meeting_archive_token_for_local_archiving",
        False,
    )
    ZOOM_WEB_IN_ARS_GET_JOIN_TOKEN_LOCAL_RECORDING = (
        "zoom",
        "zoom_web_in_ars_get_join_token_local_recording",
        False,
    )
    ZOOM_WEB_IN_ARS_GET_LIVE_STREAM_DETAILS = (
        "zoom",
        "zoom_web_in_ars_get_live_stream_details",
        False,
    )
    ZOOM_WEB_IN_ARS_UPDATE_LIVE_STREAM = (
        "zoom",
        "zoom_web_in_ars_update_live_stream",
        False,
    )
    ZOOM_WEB_IN_ARS_UPDATE_LIVE_STREAM_STATUS = (
        "zoom",
        "zoom_web_in_ars_update_live_stream_status",
        False,
    )
    ZOOM_WEB_IN_ARS_LIST_PANELISTS = ("zoom", "zoom_web_in_ars_list_panelists", False)
    ZOOM_WEB_IN_ARS_ADD_PANELISTS = ("zoom", "zoom_web_in_ars_add_panelists", False)
    ZOOM_WEB_IN_ARS_REMOVE_PANELISTS = (
        "zoom",
        "zoom_web_in_ars_remove_panelists",
        False,
    )
    ZOOM_WEB_IN_ARS_REMOVE_PANELIST = ("zoom", "zoom_web_in_ars_remove_panelist", False)
    ZOOM_WEB_IN_ARS_LIST_POLLS = ("zoom", "zoom_web_in_ars_list_polls", False)
    ZOOM_WEB_IN_ARS_CREATE_POLL = ("zoom", "zoom_web_in_ars_create_poll", False)
    ZOOM_WEB_IN_ARS_GET_POLL_DETAILS = (
        "zoom",
        "zoom_web_in_ars_get_poll_details",
        False,
    )
    ZOOM_WEB_IN_ARS_UPDATE_POLL = ("zoom", "zoom_web_in_ars_update_poll", False)
    ZOOM_WEB_IN_ARS_DELETE_POLL = ("zoom", "zoom_web_in_ars_delete_poll", False)
    ZOOM_WEB_IN_ARS_LIST_REGISTRANTS = (
        "zoom",
        "zoom_web_in_ars_list_registrants",
        False,
    )
    ZOOM_WEB_IN_ARS_ADD_REGISTRANT = ("zoom", "zoom_web_in_ars_add_registrant", False)
    ZOOM_WEB_IN_ARS_LIST_REGISTRATION_QUESTIONS = (
        "zoom",
        "zoom_web_in_ars_list_registration_questions",
        False,
    )
    ZOOM_WEB_IN_ARS_UPDATE_REGISTRATION_QUESTIONS = (
        "zoom",
        "zoom_web_in_ars_update_registration_questions",
        False,
    )
    ZOOM_WEB_IN_ARS_UPDATE_REGISTRANT_STATUS = (
        "zoom",
        "zoom_web_in_ars_update_registrant_status",
        False,
    )
    ZOOM_WEB_IN_ARS_REGISTRANT_DETAILS = (
        "zoom",
        "zoom_web_in_ars_registrant_details",
        False,
    )
    ZOOM_WEB_IN_ARS_DELETE_REGISTRANT = (
        "zoom",
        "zoom_web_in_ars_delete_registrant",
        False,
    )
    ZOOM_WEB_IN_ARS_GETS_IP_URI_WITH_PASS_CODE = (
        "zoom",
        "zoom_web_in_ars_gets_ip_uri_with_pass_code",
        False,
    )
    ZOOM_WEB_IN_ARS_UPDATE_STATUS = ("zoom", "zoom_web_in_ars_update_status", False)
    ZOOM_WEB_IN_ARS_GET_SURVEY = ("zoom", "zoom_web_in_ars_get_survey", False)
    ZOOM_WEB_IN_ARS_DELETE_SURVEY = ("zoom", "zoom_web_in_ars_delete_survey", False)
    ZOOM_WEB_IN_ARS_UPDATE_SURVEY = ("zoom", "zoom_web_in_ars_update_survey", False)
    ZOOM_WEB_IN_ARS_GET_WEB_IN_ART_OKEN = (
        "zoom",
        "zoom_web_in_ars_get_web_in_art_oken",
        False,
    )
    ZOOM_WEB_IN_ARS_LIST_TRACKING_SOURCES = (
        "zoom",
        "zoom_web_in_ars_list_tracking_sources",
        False,
    )
    LISTENNOTES_SEARCH = ("listennotes", "listennotes_search", False)
    LISTENNOTES_TYPE_AHEAD = ("listennotes", "listennotes_type_ahead", False)
    LISTENNOTES_SEARCH_EPISODE_TITLES = (
        "listennotes",
        "listennotes_search_episode_titles",
        False,
    )
    LISTENNOTES_GET_TRENDING_SEARCHES = (
        "listennotes",
        "listennotes_get_trending_searches",
        False,
    )
    LISTENNOTES_GET_RELATED_SEARCHES = (
        "listennotes",
        "listennotes_get_related_searches",
        False,
    )
    LISTENNOTES_SPELL_CHECK = ("listennotes", "listennotes_spell_check", False)
    LISTENNOTES_GET_BEST_PODCASTS = (
        "listennotes",
        "listennotes_get_best_podcasts",
        False,
    )
    LISTENNOTES_GET_PODCAST_BY_ID = (
        "listennotes",
        "listennotes_get_podcast_by_id",
        False,
    )
    LISTENNOTES_DELETE_PODCAST_BY_ID = (
        "listennotes",
        "listennotes_delete_podcast_by_id",
        False,
    )
    LISTENNOTES_GET_EPISODE_BY_ID = (
        "listennotes",
        "listennotes_get_episode_by_id",
        False,
    )
    LISTENNOTES_GET_EPISODES_IN_BATCH = (
        "listennotes",
        "listennotes_get_episodes_in_batch",
        False,
    )
    LISTENNOTES_GET_PODCASTS_IN_BATCH = (
        "listennotes",
        "listennotes_get_podcasts_in_batch",
        False,
    )
    LISTENNOTES_GET_CURATED_PODCAST_BY_ID = (
        "listennotes",
        "listennotes_get_curated_podcast_by_id",
        False,
    )
    LISTENNOTES_GET_GENRES = ("listennotes", "listennotes_get_genres", False)
    LISTENNOTES_GET_REGIONS = ("listennotes", "listennotes_get_regions", False)
    LISTENNOTES_GET_LANGUAGES = ("listennotes", "listennotes_get_languages", False)
    LISTENNOTES_JUST_LISTEN = ("listennotes", "listennotes_just_listen", False)
    LISTENNOTES_GET_CURATED_PODCASTS = (
        "listennotes",
        "listennotes_get_curated_podcasts",
        False,
    )
    LISTENNOTES_GET_PODCAST_RECOMMENDATIONS = (
        "listennotes",
        "listennotes_get_podcast_recommendations",
        False,
    )
    LISTENNOTES_GET_EPISODE_RECOMMENDATIONS = (
        "listennotes",
        "listennotes_get_episode_recommendations",
        False,
    )
    LISTENNOTES_SUBMIT_PODCAST = ("listennotes", "listennotes_submit_podcast", False)
    LISTENNOTES_REFRESH_RSS = ("listennotes", "listennotes_refresh_rss", False)
    LISTENNOTES_GET_PLAYLIST_BY_ID = (
        "listennotes",
        "listennotes_get_playlist_by_id",
        False,
    )
    LISTENNOTES_GET_PLAYLISTS = ("listennotes", "listennotes_get_playlists", False)
    LISTENNOTES_GET_PODCAST_AUDIENCE = (
        "listennotes",
        "listennotes_get_podcast_audience",
        False,
    )
    LISTENNOTES_GET_PODCASTS_BY_DOMAIN_NAME = (
        "listennotes",
        "listennotes_get_podcasts_by_domain_name",
        False,
    )
    ELEVENLABS_GET_GENERATED_ITEMSV1_HISTORY_GET = (
        "elevenlabs",
        "elevenlabs_get_generated_itemsv1_history_get",
        False,
    )
    ELEVENLABS_GET_HISTORY_ITEM_BY_IDV1_HISTORY_HISTORY_ITEMID_GET = (
        "elevenlabs",
        "elevenlabs_get_history_item_by_idv1_history_history_itemid_get",
        False,
    )
    ELEVENLABS_DELETE_HISTORY_ITEMV1_HISTORY_HISTORY_ITEMID_DELETE = (
        "elevenlabs",
        "elevenlabs_delete_history_itemv1_history_history_itemid_delete",
        False,
    )
    ELEVENLABS_GET_AUDIO_FROM_HISTORY_ITEMV1_HISTORY_HISTORY_ITEMID_AUDIO_GET = (
        "elevenlabs",
        "elevenlabs_get_audio_from_history_itemv1_history_history_itemid_audio_get",
        False,
    )
    ELEVENLABS_DOWNLOAD_HISTORY_ITEMSV1_HISTORY_DOWNLOAD_POST = (
        "elevenlabs",
        "elevenlabs_download_history_itemsv1_history_download_post",
        False,
    )
    ELEVENLABS_DELETE_SAMPLEV1_VOICES_VOICE_ID_SAMPLES_SAMPLE_ID_DELETE = (
        "elevenlabs",
        "elevenlabs_delete_samplev1_voices_voice_id_samples_sample_id_delete",
        False,
    )
    ELEVENLABS_GET_AUDIO_FROM_SAMPLEV1_VOICES_VOICE_ID_SAMPLES_SAMPLE_ID_AUDIO_GET = (
        "elevenlabs",
        "elevenlabs_get_audio_from_samplev1_voices_voice_id_samples_sample_id_audio_get",
        False,
    )
    ELEVENLABS_TEXT_TO_SPEECHV1_TEXT_TO_SPEECH_VOICE_ID_POST = (
        "elevenlabs",
        "elevenlabs_text_to_speechv1_text_to_speech_voice_id_post",
        False,
    )
    ELEVENLABS_TEXT_TO_SPEECHV1_TEXT_TO_SPEECH_VOICE_ID_STREAM_POST = (
        "elevenlabs",
        "elevenlabs_text_to_speechv1_text_to_speech_voice_id_stream_post",
        False,
    )
    ELEVENLABS_SPEECH_TO_SPEECHV1_SPEECH_TO_SPEECH_VOICE_ID_POST = (
        "elevenlabs",
        "elevenlabs_speech_to_speechv1_speech_to_speech_voice_id_post",
        False,
    )
    ELEVENLABS_SPEECH_TO_SPEECH_STREAMINGV1_SPEECH_TO_SPEECH_VOICE_ID_STREAM_POST = (
        "elevenlabs",
        "elevenlabs_speech_to_speech_streamingv1_speech_to_speech_voice_id_stream_post",
        False,
    )
    ELEVENLABS_VOICE_GENERATION_PARAMETERSV1_VOICE_GENERATION_GENERATE_VOICE_PARAMETERS_GET = (
        "elevenlabs",
        "elevenlabs_voice_generation_parametersv1_voice_generation_generate_voice_parameters_get",
        False,
    )
    ELEVENLABS_GENERATEA_RANDOM_VOICEV1_VOICE_GENERATION_GENERATE_VOICE_POST = (
        "elevenlabs",
        "elevenlabs_generatea_random_voicev1_voice_generation_generate_voice_post",
        False,
    )
    ELEVENLABS_CREATEA_PREVIOUSLY_GENERATED_VOICEV1_VOICE_GENERATION_CREATE_VOICE_POST = (
        "elevenlabs",
        "elevenlabs_createa_previously_generated_voicev1_voice_generation_create_voice_post",
        False,
    )
    ELEVENLABS_GET_USER_SUBSCRIPTION_INFOV1_USER_SUBSCRIPTION_GET = (
        "elevenlabs",
        "elevenlabs_get_user_subscription_infov1_user_subscription_get",
        False,
    )
    ELEVENLABS_GET_USER_INFOV1_USER_GET = (
        "elevenlabs",
        "elevenlabs_get_user_infov1_user_get",
        False,
    )
    ELEVENLABS_GET_VOICESV1_VOICES_GET = (
        "elevenlabs",
        "elevenlabs_get_voicesv1_voices_get",
        False,
    )
    ELEVENLABS_GET_DEFAULT_VOICE_SETTINGSV1_VOICES_SETTINGS_DEFAULT_GET = (
        "elevenlabs",
        "elevenlabs_get_default_voice_settingsv1_voices_settings_default_get",
        False,
    )
    ELEVENLABS_GET_VOICE_SETTINGSV1_VOICES_VOICE_ID_SETTINGS_GET = (
        "elevenlabs",
        "elevenlabs_get_voice_settingsv1_voices_voice_id_settings_get",
        False,
    )
    ELEVENLABS_GET_VOICEV1_VOICES_VOICE_ID_GET = (
        "elevenlabs",
        "elevenlabs_get_voicev1_voices_voice_id_get",
        False,
    )
    ELEVENLABS_DELETE_VOICEV1_VOICES_VOICE_ID_DELETE = (
        "elevenlabs",
        "elevenlabs_delete_voicev1_voices_voice_id_delete",
        False,
    )
    ELEVENLABS_EDIT_VOICE_SETTINGSV1_VOICES_VOICE_ID_SETTINGS_EDIT_POST = (
        "elevenlabs",
        "elevenlabs_edit_voice_settingsv1_voices_voice_id_settings_edit_post",
        False,
    )
    ELEVENLABS_ADD_VOICEV1_VOICES_ADD_POST = (
        "elevenlabs",
        "elevenlabs_add_voicev1_voices_add_post",
        False,
    )
    ELEVENLABS_EDIT_VOICEV1_VOICES_VOICE_ID_EDIT_POST = (
        "elevenlabs",
        "elevenlabs_edit_voicev1_voices_voice_id_edit_post",
        False,
    )
    ELEVENLABS_ADD_SHARING_VOICEV1_VOICES_ADD_PUBLIC_USE_RID_VOICE_ID_POST = (
        "elevenlabs",
        "elevenlabs_add_sharing_voicev1_voices_add_public_use_rid_voice_id_post",
        False,
    )
    ELEVENLABS_GET_PROJECTSV1_PROJECTS_GET = (
        "elevenlabs",
        "elevenlabs_get_projectsv1_projects_get",
        False,
    )
    ELEVENLABS_ADD_PROJECTV1_PROJECTS_ADD_POST = (
        "elevenlabs",
        "elevenlabs_add_projectv1_projects_add_post",
        False,
    )
    ELEVENLABS_GET_PROJECT_BY_IDV1_PROJECTS_PROJECT_ID_GET = (
        "elevenlabs",
        "elevenlabs_get_project_by_idv1_projects_project_id_get",
        False,
    )
    ELEVENLABS_DELETE_PROJECTV1_PROJECTS_PROJECT_ID_DELETE = (
        "elevenlabs",
        "elevenlabs_delete_projectv1_projects_project_id_delete",
        False,
    )
    ELEVENLABS_CONVERT_PROJECTV1_PROJECTS_PROJECT_ID_CONVERT_POST = (
        "elevenlabs",
        "elevenlabs_convert_projectv1_projects_project_id_convert_post",
        False,
    )
    ELEVENLABS_GET_PROJECT_SNAPSHOTSV1_PROJECTS_PROJECT_ID_SNAPSHOTS_GET = (
        "elevenlabs",
        "elevenlabs_get_project_snapshotsv1_projects_project_id_snapshots_get",
        False,
    )
    ELEVENLABS_STREAM_PROJECT_AUDIOV1_PROJECTS_PROJECT_ID_SNAPSHOTS_PROJECT_SNAPSHOT_ID_STREAM_POST = (
        "elevenlabs",
        "elevenlabs_stream_project_audiov1_projects_project_id_snapshots_project_snapshot_id_stream_post",
        False,
    )
    ELEVENLABS_STREAMS_ARCHIVE_WITH_PROJECT_AUDIOV1_PROJECTS_PROJECT_ID_SNAPSHOTS_PROJECT_SNAPSHOT_ID_ARCHIVE_POST = (
        "elevenlabs",
        "elevenlabs_streams_archive_with_project_audiov1_projects_project_id_snapshots_project_snapshot_id_archive_post",
        False,
    )
    ELEVENLABS_GET_CHAPTERSV1_PROJECTS_PROJECT_ID_CHAPTERS_GET = (
        "elevenlabs",
        "elevenlabs_get_chaptersv1_projects_project_id_chapters_get",
        False,
    )
    ELEVENLABS_GET_CHAPTER_BY_IDV1_PROJECTS_PROJECT_ID_CHAPTERS_CHAPTER_ID_GET = (
        "elevenlabs",
        "elevenlabs_get_chapter_by_idv1_projects_project_id_chapters_chapter_id_get",
        False,
    )
    ELEVENLABS_DELETE_CHAPTERV1_PROJECTS_PROJECT_ID_CHAPTERS_CHAPTER_ID_DELETE = (
        "elevenlabs",
        "elevenlabs_delete_chapterv1_projects_project_id_chapters_chapter_id_delete",
        False,
    )
    ELEVENLABS_CONVERT_CHAPTERV1_PROJECTS_PROJECT_ID_CHAPTERS_CHAPTER_ID_CONVERT_POST = (
        "elevenlabs",
        "elevenlabs_convert_chapterv1_projects_project_id_chapters_chapter_id_convert_post",
        False,
    )
    ELEVENLABS_GET_CHAPTER_SNAPSHOTSV1_PROJECTS_PROJECT_ID_CHAPTERS_CHAPTER_ID_SNAPSHOTS_GET = (
        "elevenlabs",
        "elevenlabs_get_chapter_snapshotsv1_projects_project_id_chapters_chapter_id_snapshots_get",
        False,
    )
    ELEVENLABS_STREAM_CHAPTER_AUDIOV1_PROJECTS_PROJECT_ID_CHAPTERS_CHAPTER_ID_SNAPSHOTS_CHAPTER_SNAPSHOT_ID_STREAM_POST = (
        "elevenlabs",
        "elevenlabs_stream_chapter_audiov1_projects_project_id_chapters_chapter_id_snapshots_chapter_snapshot_id_stream_post",
        False,
    )
    ELEVENLABS_UPDATE_PRONUNCIATION_DICTIONARIESV1_PROJECTS_PROJECT_ID_UPDATE_PRONUNCIATION_DICTIONARIES_POST = (
        "elevenlabs",
        "elevenlabs_update_pronunciation_dictionariesv1_projects_project_id_update_pronunciation_dictionaries_post",
        False,
    )
    ELEVENLABS_DUBA_VIDEO_OR_AN_AUDIOFILEV1_DUBBING_POST = (
        "elevenlabs",
        "elevenlabs_duba_video_or_an_audiofilev1_dubbing_post",
        False,
    )
    ELEVENLABS_GET_DUBBING_PROJECT_METADATAV1_DUBBING_DUBBING_ID_GET = (
        "elevenlabs",
        "elevenlabs_get_dubbing_project_metadatav1_dubbing_dubbing_id_get",
        False,
    )
    ELEVENLABS_DELETE_DUBBING_PROJECTV1_DUBBING_DUBBING_ID_DELETE = (
        "elevenlabs",
        "elevenlabs_delete_dubbing_projectv1_dubbing_dubbing_id_delete",
        False,
    )
    ELEVENLABS_GET_DUBBED_FILEV1_DUBBING_DUBBING_ID_AUDIO_LANGUAGE_CODE_GET = (
        "elevenlabs",
        "elevenlabs_get_dubbed_filev1_dubbing_dubbing_id_audio_language_code_get",
        False,
    )
    ELEVENLABS_GET_TRANSCRIPT_FOR_DUBV1_DUBBING_DUBBING_ID_TRANSCRIPT_LANGUAGE_CODE_GET = (
        "elevenlabs",
        "elevenlabs_get_transcript_for_dubv1_dubbing_dubbing_id_transcript_language_code_get",
        False,
    )
    ELEVENLABS_GETS_SO_PROVIDER_ADMIN_ADMIN_ADMIN_URL_PREFIXS_SO_PROVIDER_GET = (
        "elevenlabs",
        "elevenlabs_gets_so_provider_admin_admin_admin_url_prefixs_so_provider_get",
        False,
    )
    ELEVENLABS_GET_MODELSV1_MODELS_GET = (
        "elevenlabs",
        "elevenlabs_get_modelsv1_models_get",
        False,
    )
    ELEVENLABS_CREATES_AUDIO_NATIVE_ENABLED_PROJECTV1_AUDIO_NATIVE_POST = (
        "elevenlabs",
        "elevenlabs_creates_audio_native_enabled_projectv1_audio_native_post",
        False,
    )
    ELEVENLABS_GET_VOICESV1_SHARED_VOICES_GET = (
        "elevenlabs",
        "elevenlabs_get_voicesv1_shared_voices_get",
        False,
    )
    ELEVENLABS_ADDA_PRONUNCIATION_DICTIONARYV1_PRONUNCIATION_DICTIONARIES_ADD_FROM_FILE_POST = (
        "elevenlabs",
        "elevenlabs_adda_pronunciation_dictionaryv1_pronunciation_dictionaries_add_from_file_post",
        False,
    )
    ELEVENLABS_ADD_RULES_TO_THE_PRONUNCIATION_DICTIONARYV1_PRONUNCIATION_DICTIONARIES_PRONUNCIATION_DICTIONARY_ID_ADD_RULES_POST = (
        "elevenlabs",
        "elevenlabs_add_rules_to_the_pronunciation_dictionaryv1_pronunciation_dictionaries_pronunciation_dictionary_id_add_rules_post",
        False,
    )
    ELEVENLABS_REMOVE_RULES_FROM_THE_PRONUNCIATION_DICTIONARYV1_PRONUNCIATION_DICTIONARIES_PRONUNCIATION_DICTIONARY_ID_REMOVE_RULES_POST = (
        "elevenlabs",
        "elevenlabs_remove_rules_from_the_pronunciation_dictionaryv1_pronunciation_dictionaries_pronunciation_dictionary_id_remove_rules_post",
        False,
    )
    ELEVENLABS_GET_PLS_FILE_WITHA_PRONUNCIATION_DICTIONARY_VERSION_RULESV1_PRONUNCIATION_DICTIONARIES_DICTIONARY_ID_VERSION_ID_DOWNLOAD_GET = (
        "elevenlabs",
        "elevenlabs_get_pls_file_witha_pronunciation_dictionary_version_rulesv1_pronunciation_dictionaries_dictionary_id_version_id_download_get",
        False,
    )
    ELEVENLABS_GET_METADATA_FORA_PRONUNCIATION_DICTIONARYV1_PRONUNCIATION_DICTIONARIES_PRONUNCIATION_DICTIONARY_ID_GET = (
        "elevenlabs",
        "elevenlabs_get_metadata_fora_pronunciation_dictionaryv1_pronunciation_dictionaries_pronunciation_dictionary_id_get",
        False,
    )
    ELEVENLABS_GET_PRONUNCIATION_DICTIONARIESV1_PRONUNCIATION_DICTIONARIES_GET = (
        "elevenlabs",
        "elevenlabs_get_pronunciation_dictionariesv1_pronunciation_dictionaries_get",
        False,
    )
    ELEVENLABS_GETA_PROFILE_PAGE_PROFILE_HANDLE_GET = (
        "elevenlabs",
        "elevenlabs_geta_profile_page_profile_handle_get",
        False,
    )
    ELEVENLABS_REDIRECT_TO_MINT_LI_FY_DOCS_GET = (
        "elevenlabs",
        "elevenlabs_redirect_to_mint_li_fy_docs_get",
        False,
    )
    BREVO_EMAIL_CAMPAIGNS_GET_ALL = ("brevo", "brevo_email_campaigns_get_all", False)
    BREVO_EMAIL_CAMPAIGNS_CREATE_CAMPAIGN = (
        "brevo",
        "brevo_email_campaigns_create_campaign",
        False,
    )
    BREVO_EMAIL_CAMPAIGNS_GET_REPORT = (
        "brevo",
        "brevo_email_campaigns_get_report",
        False,
    )
    BREVO_EMAIL_CAMPAIGNS_UPDATE_CAMPAIGN = (
        "brevo",
        "brevo_email_campaigns_update_campaign",
        False,
    )
    BREVO_EMAIL_CAMPAIGNS_REMOVE_CAMPAIGN = (
        "brevo",
        "brevo_email_campaigns_remove_campaign",
        False,
    )
    BREVO_EMAIL_CAMPAIGNS_SEND_IMMEDIATE = (
        "brevo",
        "brevo_email_campaigns_send_immediate",
        False,
    )
    BREVO_EMAIL_CAMPAIGNS_SEND_TEST_TO_TEST_LIST = (
        "brevo",
        "brevo_email_campaigns_send_test_to_test_list",
        False,
    )
    BREVO_EMAIL_CAMPAIGNS_UPDATE_STATUS = (
        "brevo",
        "brevo_email_campaigns_update_status",
        False,
    )
    BREVO_EMAIL_CAMPAIGNS_SEND_REPORT = (
        "brevo",
        "brevo_email_campaigns_send_report",
        False,
    )
    BREVO_EMAIL_CAMPAIGNS_GET_AB_TEST_RESULT = (
        "brevo",
        "brevo_email_campaigns_get_ab_test_result",
        False,
    )
    BREVO_EMAIL_CAMPAIGNS_GET_SHARED_URL = (
        "brevo",
        "brevo_email_campaigns_get_shared_url",
        False,
    )
    BREVO_EMAIL_CAMPAIGNS_EXPORT_RECIPIENTS_POST = (
        "brevo",
        "brevo_email_campaigns_export_recipients_post",
        False,
    )
    BREVO_EMAIL_CAMPAIGNS_UPLOAD_IMAGE_TO_GALLERY = (
        "brevo",
        "brevo_email_campaigns_upload_image_to_gallery",
        False,
    )
    BREVO_TRANSACTIONAL_EMAILS_SEND_TRANSACTIONAL_EMAIL = (
        "brevo",
        "brevo_transactional_emails_send_transactional_email",
        False,
    )
    BREVO_TRANSACTIONAL_EMAILS_GET_LIST = (
        "brevo",
        "brevo_transactional_emails_get_list",
        False,
    )
    BREVO_TRANSACTIONAL_EMAILS_GET_CONTENT_BYUU_ID = (
        "brevo",
        "brevo_transactional_emails_get_content_byuu_id",
        False,
    )
    BREVO_TRANSACTIONAL_EMAILS_DELETE_LOG = (
        "brevo",
        "brevo_transactional_emails_delete_log",
        False,
    )
    BREVO_TRANSACTIONAL_EMAILS_LIST_TEMPLATES = (
        "brevo",
        "brevo_transactional_emails_list_templates",
        False,
    )
    BREVO_TRANSACTIONAL_EMAILS_CREATE_TEMPLATE = (
        "brevo",
        "brevo_transactional_emails_create_template",
        False,
    )
    BREVO_TRANSACTIONAL_EMAILS_GET_TEMPLATE_INFO = (
        "brevo",
        "brevo_transactional_emails_get_template_info",
        False,
    )
    BREVO_TRANSACTIONAL_EMAILS_UPDATE_TEMPLATE = (
        "brevo",
        "brevo_transactional_emails_update_template",
        False,
    )
    BREVO_TRANSACTIONAL_EMAILS_DELETE_TEMPLATE_BY_ID = (
        "brevo",
        "brevo_transactional_emails_delete_template_by_id",
        False,
    )
    BREVO_TRANSACTIONAL_EMAILS_SEND_TEST_TEMPLATE = (
        "brevo",
        "brevo_transactional_emails_send_test_template",
        False,
    )
    BREVO_TRANSACTIONAL_EMAILS_GET_AGGREGATED_REPORT = (
        "brevo",
        "brevo_transactional_emails_get_aggregated_report",
        False,
    )
    BREVO_TRANSACTIONAL_EMAILS_GET_ACTIVITY_PER_DAY = (
        "brevo",
        "brevo_transactional_emails_get_activity_per_day",
        False,
    )
    BREVO_TRANSACTIONAL_EMAILS_GET_ALL_ACTIVITY = (
        "brevo",
        "brevo_transactional_emails_get_all_activity",
        False,
    )
    BREVO_TRANSACTIONAL_EMAILS_UNBLOCK_CONTACT = (
        "brevo",
        "brevo_transactional_emails_unblock_contact",
        False,
    )
    BREVO_TRANSACTIONAL_EMAILS_LIST_BLOCKED_CONTACTS = (
        "brevo",
        "brevo_transactional_emails_list_blocked_contacts",
        False,
    )
    BREVO_TRANSACTIONAL_EMAILS_GET_BLOCKED_DOMAINS = (
        "brevo",
        "brevo_transactional_emails_get_blocked_domains",
        False,
    )
    BREVO_TRANSACTIONAL_EMAILS_ADD_BLOCKED_DOMAIN = (
        "brevo",
        "brevo_transactional_emails_add_blocked_domain",
        False,
    )
    BREVO_TRANSACTIONAL_EMAILS_UNBLOCK_DOMAIN = (
        "brevo",
        "brevo_transactional_emails_unblock_domain",
        False,
    )
    BREVO_TRANSACTIONAL_EMAILS_REMOVE_HARD_BOUNCES = (
        "brevo",
        "brevo_transactional_emails_remove_hard_bounces",
        False,
    )
    BREVO_TRANSACTIONAL_EMAILS_GET_EMAIL_STATUS_BY_ID = (
        "brevo",
        "brevo_transactional_emails_get_email_status_by_id",
        False,
    )
    BREVO_TRANSACTIONAL_EMAILS_DELETE_SCHEDULED_EMAILS = (
        "brevo",
        "brevo_transactional_emails_delete_scheduled_emails",
        False,
    )
    BREVO_CONTACTS_GET_ALL_CONTACTS = (
        "brevo",
        "brevo_contacts_get_all_contacts",
        False,
    )
    BREVO_CONTACTS_CREATE_NEW_CONTACT = (
        "brevo",
        "brevo_contacts_create_new_contact",
        False,
    )
    BREVO_CONTACTS_CREATE_DOUBLE_OPT_IN_CONTACT = (
        "brevo",
        "brevo_contacts_create_double_opt_in_contact",
        False,
    )
    BREVO_CONTACTS_GET_DETAILS = ("brevo", "brevo_contacts_get_details", False)
    BREVO_CONTACTS_DELETE_CONTACT = ("brevo", "brevo_contacts_delete_contact", False)
    BREVO_CONTACTS_UPDATE_CONTACT_BY_ID = (
        "brevo",
        "brevo_contacts_update_contact_by_id",
        False,
    )
    BREVO_CONTACTS_UPDATE_MULTIPLE = ("brevo", "brevo_contacts_update_multiple", False)
    BREVO_CONTACTS_GET_EMAIL_CAMPAIGN_STATS = (
        "brevo",
        "brevo_contacts_get_email_campaign_stats",
        False,
    )
    BREVO_CONTACTS_LIST_ATTRIBUTES = ("brevo", "brevo_contacts_list_attributes", False)
    BREVO_CONTACTS_UPDATE_ATTRIBUTE = (
        "brevo",
        "brevo_contacts_update_attribute",
        False,
    )
    BREVO_CONTACTS_CREATE_ATTRIBUTE = (
        "brevo",
        "brevo_contacts_create_attribute",
        False,
    )
    BREVO_CONTACTS_REMOVE_ATTRIBUTE = (
        "brevo",
        "brevo_contacts_remove_attribute",
        False,
    )
    BREVO_CONTACTS_GET_ALL_FOLDERS = ("brevo", "brevo_contacts_get_all_folders", False)
    BREVO_CONTACTS_CREATE_FOLDER = ("brevo", "brevo_contacts_create_folder", False)
    BREVO_CONTACTS_GET_FOLDER_DETAILS = (
        "brevo",
        "brevo_contacts_get_folder_details",
        False,
    )
    BREVO_CONTACTS_UPDATE_FOLDER = ("brevo", "brevo_contacts_update_folder", False)
    BREVO_CONTACTS_DELETE_FOLDER = ("brevo", "brevo_contacts_delete_folder", False)
    BREVO_CONTACTS_GET_FOLDER_LISTS = (
        "brevo",
        "brevo_contacts_get_folder_lists",
        False,
    )
    BREVO_CONTACTS_GET_ALL_LISTS = ("brevo", "brevo_contacts_get_all_lists", False)
    BREVO_CONTACTS_CREATE_LIST = ("brevo", "brevo_contacts_create_list", False)
    BREVO_CONTACTS_GET_LIST_DETAILS = (
        "brevo",
        "brevo_contacts_get_list_details",
        False,
    )
    BREVO_CONTACTS_UPDATE_LIST = ("brevo", "brevo_contacts_update_list", False)
    BREVO_CONTACTS_DELETE_LIST = ("brevo", "brevo_contacts_delete_list", False)
    BREVO_CONTACTS_GET_ALL_SEGMENTS = (
        "brevo",
        "brevo_contacts_get_all_segments",
        False,
    )
    BREVO_CONTACTS_GET_LIST_CONTACTS = (
        "brevo",
        "brevo_contacts_get_list_contacts",
        False,
    )
    BREVO_CONTACTS_ADD_TO_LIST = ("brevo", "brevo_contacts_add_to_list", False)
    BREVO_CONTACTS_REMOVE_CONTACT_FROM_LIST = (
        "brevo",
        "brevo_contacts_remove_contact_from_list",
        False,
    )
    BREVO_CONTACTS_EXPORT_PROCESS_ID = (
        "brevo",
        "brevo_contacts_export_process_id",
        False,
    )
    BREVO_CONTACTS_IMPORT_CONTACTS_PROCESS = (
        "brevo",
        "brevo_contacts_import_contacts_process",
        False,
    )
    BREVO_SMS_CAMPAIGNS_GET_ALL_INFORMATION = (
        "brevo",
        "brevo_sms_campaigns_get_all_information",
        False,
    )
    BREVO_SMS_CAMPAIGNS_CREATE_CAMPAIGN = (
        "brevo",
        "brevo_sms_campaigns_create_campaign",
        False,
    )
    BREVO_SMS_CAMPAIGNS_GET_CAMPAIGN_BY_ID = (
        "brevo",
        "brevo_sms_campaigns_get_campaign_by_id",
        False,
    )
    BREVO_SMS_CAMPAIGNS_UPDATE_CAMPAIGN_BY_ID = (
        "brevo",
        "brevo_sms_campaigns_update_campaign_by_id",
        False,
    )
    BREVO_SMS_CAMPAIGNS_REMOVE_CAMPAIGN_BY_ID = (
        "brevo",
        "brevo_sms_campaigns_remove_campaign_by_id",
        False,
    )
    BREVO_SMS_CAMPAIGNS_SEND_IMMEDIATELY = (
        "brevo",
        "brevo_sms_campaigns_send_immediately",
        False,
    )
    BREVO_SMS_CAMPAIGNS_UPDATE_STATUS = (
        "brevo",
        "brevo_sms_campaigns_update_status",
        False,
    )
    BREVO_SMS_CAMPAIGNS_SEND_TESTS_MS = (
        "brevo",
        "brevo_sms_campaigns_send_tests_ms",
        False,
    )
    BREVO_SMS_CAMPAIGNS_EXPORT_RECIPIENTS_PROCESS = (
        "brevo",
        "brevo_sms_campaigns_export_recipients_process",
        False,
    )
    BREVO_SMS_CAMPAIGNS_SEND_CAMPAIGN_REPORT = (
        "brevo",
        "brevo_sms_campaigns_send_campaign_report",
        False,
    )
    BREVO_TRANSACTIONAL_SMS_SENDS_MS_MESSAGE_TO_MOBILE = (
        "brevo",
        "brevo_transactional_sms_sends_ms_message_to_mobile",
        False,
    )
    BREVO_TRANSACTIONAL_SMS_GET_AGGREGATED_REPORT = (
        "brevo",
        "brevo_transactional_sms_get_aggregated_report",
        False,
    )
    BREVO_TRANSACTIONAL_SMS_GETS_MS_ACTIVITY_AGGREGATED_PER_DAY = (
        "brevo",
        "brevo_transactional_sms_gets_ms_activity_aggregated_per_day",
        False,
    )
    BREVO_TRANSACTIONAL_SMS_GET_ALL_EVENTS = (
        "brevo",
        "brevo_transactional_sms_get_all_events",
        False,
    )
    BREVO_WHATS_APP_CAMPAIGNS_GET_CAMPAIGN_BY_ID = (
        "brevo",
        "brevo_whats_app_campaigns_get_campaign_by_id",
        False,
    )
    BREVO_WHATS_APP_CAMPAIGNS_DELETE_CAMPAIGN = (
        "brevo",
        "brevo_whats_app_campaigns_delete_campaign",
        False,
    )
    BREVO_WHATS_APP_CAMPAIGNS_UPDATE_CAMPAIGN_BY_ID = (
        "brevo",
        "brevo_whats_app_campaigns_update_campaign_by_id",
        False,
    )
    BREVO_WHATS_APP_CAMPAIGNS_GET_TEMPLATES = (
        "brevo",
        "brevo_whats_app_campaigns_get_templates",
        False,
    )
    BREVO_WHATS_APP_CAMPAIGNS_CREATE_AND_SEND = (
        "brevo",
        "brevo_whats_app_campaigns_create_and_send",
        False,
    )
    BREVO_WHATS_APP_CAMPAIGNS_GET_ALL = (
        "brevo",
        "brevo_whats_app_campaigns_get_all",
        False,
    )
    BREVO_WHATS_APP_CAMPAIGNS_CREATE_TEMPLATE = (
        "brevo",
        "brevo_whats_app_campaigns_create_template",
        False,
    )
    BREVO_WHATS_APP_CAMPAIGNS_SEND_TEMPLATE_FOR_APPROVAL = (
        "brevo",
        "brevo_whats_app_campaigns_send_template_for_approval",
        False,
    )
    BREVO_WHATS_APP_CAMPAIGNS_GET_ACCOUNT_INFO = (
        "brevo",
        "brevo_whats_app_campaigns_get_account_info",
        False,
    )
    BREVO_SENDERS_LIST_ALL = ("brevo", "brevo_senders_list_all", False)
    BREVO_SENDERS_CREATE_NEW_SENDER = (
        "brevo",
        "brevo_senders_create_new_sender",
        False,
    )
    BREVO_SENDERS_UPDATES_ENDERBY_ID = (
        "brevo",
        "brevo_senders_updates_enderby_id",
        False,
    )
    BREVO_SENDERS_REMOVE_SENDER = ("brevo", "brevo_senders_remove_sender", False)
    BREVO_SENDERS_VALIDATE_SENDER_USING_OTP = (
        "brevo",
        "brevo_senders_validate_sender_using_otp",
        False,
    )
    BREVO_SENDERS_GET_ALL_DEDICATED_IPS = (
        "brevo",
        "brevo_senders_get_all_dedicated_ips",
        False,
    )
    BREVO_SENDERS_GET_DEDICATED_IPS = (
        "brevo",
        "brevo_senders_get_dedicated_ips",
        False,
    )
    BREVO_DOMAINS_GET_ALL = ("brevo", "brevo_domains_get_all", False)
    BREVO_DOMAINS_CREATE_NEW_DOMAIN = (
        "brevo",
        "brevo_domains_create_new_domain",
        False,
    )
    BREVO_DOMAINS_DELETE_DOMAIN = ("brevo", "brevo_domains_delete_domain", False)
    BREVO_DOMAINS_VALIDATE_CONFIGURATION = (
        "brevo",
        "brevo_domains_validate_configuration",
        False,
    )
    BREVO_DOMAINS_AUTHENTICATE_DOMAIN = (
        "brevo",
        "brevo_domains_authenticate_domain",
        False,
    )
    BREVO_WEB_HOOKS_GET_ALL = ("brevo", "brevo_web_hooks_get_all", False)
    BREVO_WEB_HOOKS_CREATE_HOOK = ("brevo", "brevo_web_hooks_create_hook", False)
    BREVO_WEB_HOOKS_GET_DETAILS = ("brevo", "brevo_web_hooks_get_details", False)
    BREVO_WEB_HOOKS_UPDATE_WEB_HOOK_BY_ID = (
        "brevo",
        "brevo_web_hooks_update_web_hook_by_id",
        False,
    )
    BREVO_WEB_HOOKS_DELETE_WEB_HOOK = (
        "brevo",
        "brevo_web_hooks_delete_web_hook",
        False,
    )
    BREVO_WEB_HOOKS_EXPORT_ALL_EVENTS = (
        "brevo",
        "brevo_web_hooks_export_all_events",
        False,
    )
    BREVO_RESELLER_LIST_CHILDREN_ACCOUNTS = (
        "brevo",
        "brevo_reseller_list_children_accounts",
        False,
    )
    BREVO_RESELLER_CREATE_CHILD = ("brevo", "brevo_reseller_create_child", False)
    BREVO_RESELLER_GET_CHILD_DETAILS = (
        "brevo",
        "brevo_reseller_get_child_details",
        False,
    )
    BREVO_RESELLER_UPDATE_CHILD_INFO = (
        "brevo",
        "brevo_reseller_update_child_info",
        False,
    )
    BREVO_RESELLER_DELETE_CHILD_BY_IDENTIFIER = (
        "brevo",
        "brevo_reseller_delete_child_by_identifier",
        False,
    )
    BREVO_RESELLER_UPDATE_CHILD_ACCOUNT_STATUS = (
        "brevo",
        "brevo_reseller_update_child_account_status",
        False,
    )
    BREVO_RESELLER_GET_CHILD_ACCOUNT_CREATION_STATUS = (
        "brevo",
        "brevo_reseller_get_child_account_creation_status",
        False,
    )
    BREVO_RESELLER_ASSOCIATE_DEDICATED_IP_TO_CHILD = (
        "brevo",
        "brevo_reseller_associate_dedicated_ip_to_child",
        False,
    )
    BREVO_RESELLER_DISSOCIATE_IP_TO_CHILD = (
        "brevo",
        "brevo_reseller_dissociate_ip_to_child",
        False,
    )
    BREVO_RESELLER_ADD_CHILD_CREDITS = (
        "brevo",
        "brevo_reseller_add_child_credits",
        False,
    )
    BREVO_RESELLER_REMOVE_CREDITS_FROM_CHILD = (
        "brevo",
        "brevo_reseller_remove_credits_from_child",
        False,
    )
    BREVO_RESELLER_GET_CHILD_DOMAINS = (
        "brevo",
        "brevo_reseller_get_child_domains",
        False,
    )
    BREVO_RESELLER_CREATE_CHILD_DOMAIN = (
        "brevo",
        "brevo_reseller_create_child_domain",
        False,
    )
    BREVO_RESELLER_UPDATE_SENDER_DOMAIN = (
        "brevo",
        "brevo_reseller_update_sender_domain",
        False,
    )
    BREVO_RESELLER_DELETE_SENDER_DOMAIN_BY_CHILD_IDENTIFIER_AND_DOMAIN_NAME = (
        "brevo",
        "brevo_reseller_delete_sender_domain_by_child_identifier_and_domain_name",
        False,
    )
    BREVO_RESELLER_GET_SESSION_TOKEN = (
        "brevo",
        "brevo_reseller_get_session_token",
        False,
    )
    BREVO_ACCOUNT_INFORMATION_DETAILS = (
        "brevo",
        "brevo_account_information_details",
        False,
    )
    BREVO_ACCOUNT_GET_USER_ACTIVITY_LOGS = (
        "brevo",
        "brevo_account_get_user_activity_logs",
        False,
    )
    BREVO_USER_GET_ALL_USERS = ("brevo", "brevo_user_get_all_users", False)
    BREVO_USER_CHECK_PERMISSION = ("brevo", "brevo_user_check_permission", False)
    BREVO_USER_REVOKE_PERMISSION_BY_EMAIL = (
        "brevo",
        "brevo_user_revoke_permission_by_email",
        False,
    )
    BREVO_USER_RESEND_INVITATION = ("brevo", "brevo_user_resend_invitation", False)
    BREVO_USERS_END_INVITATION = ("brevo", "brevo_users_end_invitation", False)
    BREVO_USER_UPDATE_PERMISSIONS = ("brevo", "brevo_user_update_permissions", False)
    BREVO_PROCESS_GET_ALL_PROCESSES = (
        "brevo",
        "brevo_process_get_all_processes",
        False,
    )
    BREVO_PROCESS_GET_PROCESS_INFORMATION = (
        "brevo",
        "brevo_process_get_process_information",
        False,
    )
    BREVO_INBOUND_PARSING_GET_ALL_EVENTS = (
        "brevo",
        "brevo_inbound_parsing_get_all_events",
        False,
    )
    BREVO_INBOUND_PARSING_GET_EMAIL_EVENTS = (
        "brevo",
        "brevo_inbound_parsing_get_email_events",
        False,
    )
    BREVO_INBOUND_PARSING_GET_ATTACHMENT_BY_TOKEN = (
        "brevo",
        "brevo_inbound_parsing_get_attachment_by_token",
        False,
    )
    BREVO_MASTER_ACCOUNT_LIST_SUB_ACCOUNTS = (
        "brevo",
        "brevo_master_account_list_sub_accounts",
        False,
    )
    BREVO_MASTER_ACCOUNT_CREATE_SUB_ACCOUNT = (
        "brevo",
        "brevo_master_account_create_sub_account",
        False,
    )
    BREVO_MASTER_ACCOUNT_GET_SUB_ACCOUNT_DETAILS = (
        "brevo",
        "brevo_master_account_get_sub_account_details",
        False,
    )
    BREVO_MASTER_ACCOUNT_DELETE_SUB_ACCOUNT = (
        "brevo",
        "brevo_master_account_delete_sub_account",
        False,
    )
    BREVO_MASTER_ACCOUNT_UPDATE_SUB_ACCOUNT_PLAN = (
        "brevo",
        "brevo_master_account_update_sub_account_plan",
        False,
    )
    BREVO_MASTER_ACCOUNT_GENERATES_SO_TOKEN = (
        "brevo",
        "brevo_master_account_generates_so_token",
        False,
    )
    BREVO_MASTER_ACCOUNT_GENERATES_SO_TOKEN2 = (
        "brevo",
        "brevo_master_account_generates_so_token2",
        False,
    )
    BREVO_MASTER_ACCOUNT_GET_DETAILS = (
        "brevo",
        "brevo_master_account_get_details",
        False,
    )
    BREVO_MASTER_ACCOUNT_CREATE_SUB_ACCOUNT_KEY = (
        "brevo",
        "brevo_master_account_create_sub_account_key",
        False,
    )
    BREVO_MASTER_ACCOUNT_ENABLE_DISABLE = (
        "brevo",
        "brevo_master_account_enable_disable",
        False,
    )
    BREVO_MASTER_ACCOUNT_CREATE_GROUP_OF_SUB_ACCOUNTS = (
        "brevo",
        "brevo_master_account_create_group_of_sub_accounts",
        False,
    )
    BREVO_MASTER_ACCOUNT_GET_GROUP_DETAILS = (
        "brevo",
        "brevo_master_account_get_group_details",
        False,
    )
    BREVO_MASTER_ACCOUNT_UPDATE_GROUP_SUB_ACCOUNTS = (
        "brevo",
        "brevo_master_account_update_group_sub_accounts",
        False,
    )
    BREVO_MASTER_ACCOUNT_DELETE_GROUP = (
        "brevo",
        "brevo_master_account_delete_group",
        False,
    )
    BREVO_MASTER_ACCOUNT_UN_LINK_SUB_ACCOUNT_FROM_GROUP = (
        "brevo",
        "brevo_master_account_un_link_sub_account_from_group",
        False,
    )
    BREVO_MASTER_ACCOUNTS_END_INVITATION_TO_ADMIN_USER = (
        "brevo",
        "brevo_master_accounts_end_invitation_to_admin_user",
        False,
    )
    BREVO_MASTER_ACCOUNT_RESEND_CANCEL_ADMIN_USER_INVITATION = (
        "brevo",
        "brevo_master_account_resend_cancel_admin_user_invitation",
        False,
    )
    BREVO_MASTER_ACCOUNT_REVOKE_ADMIN_USER = (
        "brevo",
        "brevo_master_account_revoke_admin_user",
        False,
    )
    BREVO_MASTER_ACCOUNT_LIST_ADMIN_USERS = (
        "brevo",
        "brevo_master_account_list_admin_users",
        False,
    )
    BREVO_MASTER_ACCOUNT_CHECK_ADMIN_USER_PERMISSIONS = (
        "brevo",
        "brevo_master_account_check_admin_user_permissions",
        False,
    )
    BREVO_MASTER_ACCOUNT_LIST_GROUPS = (
        "brevo",
        "brevo_master_account_list_groups",
        False,
    )
    BREVO_COMPANIES_GET_ALL = ("brevo", "brevo_companies_get_all", False)
    BREVO_COMPANIES_CREATE_COMPANY = ("brevo", "brevo_companies_create_company", False)
    BREVO_COMPANIES_GET_COMPANY_BY_ID = (
        "brevo",
        "brevo_companies_get_company_by_id",
        False,
    )
    BREVO_COMPANIES_DELETE_COMPANY = ("brevo", "brevo_companies_delete_company", False)
    BREVO_COMPANIES_UPDATE_COMPANY = ("brevo", "brevo_companies_update_company", False)
    BREVO_COMPANIES_GET_ATTRIBUTES = ("brevo", "brevo_companies_get_attributes", False)
    BREVO_COMPANIES_LINK_UN_LINK_WITH_CONTACT_DEAL = (
        "brevo",
        "brevo_companies_link_un_link_with_contact_deal",
        False,
    )
    BREVO_DEALS_GET_PIPELINE_STAGES = (
        "brevo",
        "brevo_deals_get_pipeline_stages",
        False,
    )
    BREVO_DEALS_GET_DETAILS = ("brevo", "brevo_deals_get_details", False)
    BREVO_DEALS_GET_ALL_PIPELINES = ("brevo", "brevo_deals_get_all_pipelines", False)
    BREVO_DEALS_GET_ATTRIBUTES = ("brevo", "brevo_deals_get_attributes", False)
    BREVO_DEALS_GET_ALL_DEALS = ("brevo", "brevo_deals_get_all_deals", False)
    BREVO_DEALS_CREATE_NEW_DEAL = ("brevo", "brevo_deals_create_new_deal", False)
    BREVO_DEALS_GET_BY_ID = ("brevo", "brevo_deals_get_by_id", False)
    BREVO_DEALS_DELETE_DEAL = ("brevo", "brevo_deals_delete_deal", False)
    BREVO_DEALS_UPDATE_DEAL_BY_ID = ("brevo", "brevo_deals_update_deal_by_id", False)
    BREVO_DEALS_LINK_UN_LINK_PATCH = ("brevo", "brevo_deals_link_un_link_patch", False)
    BREVO_TASKS_GET_ALL_TASK_TYPES = ("brevo", "brevo_tasks_get_all_task_types", False)
    BREVO_TASKS_GET_ALL = ("brevo", "brevo_tasks_get_all", False)
    BREVO_TASKS_CREATE_NEW_TASK = ("brevo", "brevo_tasks_create_new_task", False)
    BREVO_TASKS_GET_TASK_BY_ID = ("brevo", "brevo_tasks_get_task_by_id", False)
    BREVO_TASKS_REMOVE_TASK = ("brevo", "brevo_tasks_remove_task", False)
    BREVO_TASKS_UPDATE_TASK = ("brevo", "brevo_tasks_update_task", False)
    BREVO_NOTES_GET_ALL = ("brevo", "brevo_notes_get_all", False)
    BREVO_NOTES_CREATE_NEW_NOTE = ("brevo", "brevo_notes_create_new_note", False)
    BREVO_NOTES_GET_BY_ID = ("brevo", "brevo_notes_get_by_id", False)
    BREVO_NOTES_UPDATE_NOTE_BY_ID = ("brevo", "brevo_notes_update_note_by_id", False)
    BREVO_NOTES_REMOVE_BY_ID = ("brevo", "brevo_notes_remove_by_id", False)
    BREVO_FILES_GET_ALL_FILES = ("brevo", "brevo_files_get_all_files", False)
    BREVO_FILES_UPLOAD_FILE = ("brevo", "brevo_files_upload_file", False)
    BREVO_FILES_DOWNLOAD_FILE = ("brevo", "brevo_files_download_file", False)
    BREVO_FILES_DELETE_FILE = ("brevo", "brevo_files_delete_file", False)
    BREVO_FILES_GET_FILE_DETAILS = ("brevo", "brevo_files_get_file_details", False)
    BREVO_CONVERSATIONS_SEND_MESSAGE_AS_AGENT = (
        "brevo",
        "brevo_conversations_send_message_as_agent",
        False,
    )
    BREVO_CONVERSATIONS_GET_MESSAGE_BY_ID = (
        "brevo",
        "brevo_conversations_get_message_by_id",
        False,
    )
    BREVO_CONVERSATIONS_UPDATE_AGENT_MESSAGE = (
        "brevo",
        "brevo_conversations_update_agent_message",
        False,
    )
    BREVO_CONVERSATIONS_DELETE_MESSAGE_SENT_BY_AGENT = (
        "brevo",
        "brevo_conversations_delete_message_sent_by_agent",
        False,
    )
    BREVO_CONVERSATIONS_SEND_AUTOMATED_MESSAGE = (
        "brevo",
        "brevo_conversations_send_automated_message",
        False,
    )
    BREVO_CONVERSATIONS_GET_AUTOMATED_MESSAGE = (
        "brevo",
        "brevo_conversations_get_automated_message",
        False,
    )
    BREVO_CONVERSATIONS_UPDATE_PUSHED_MESSAGE = (
        "brevo",
        "brevo_conversations_update_pushed_message",
        False,
    )
    BREVO_CONVERSATIONS_DELETE_AUTOMATED_MESSAGE = (
        "brevo",
        "brevo_conversations_delete_automated_message",
        False,
    )
    BREVO_CONVERSATIONS_SET_AGENT_ONLINE_STATUS = (
        "brevo",
        "brevo_conversations_set_agent_online_status",
        False,
    )
    BREVO_E_COMMERCE_ACTIVATE_APP = ("brevo", "brevo_e_commerce_activate_app", False)
    BREVO_E_COMMERCE_GET_ORDERS = ("brevo", "brevo_e_commerce_get_orders", False)
    BREVO_E_COMMERCE_MANAGE_ORDER_STATUS = (
        "brevo",
        "brevo_e_commerce_manage_order_status",
        False,
    )
    BREVO_E_COMMERCE_CREATE_ORDER_BATCH = (
        "brevo",
        "brevo_e_commerce_create_order_batch",
        False,
    )
    BREVO_EVENT_TRACK_INTERACTION = ("brevo", "brevo_event_track_interaction", False)
    BREVO_E_COMMERCE_GET_ALL_CATEGORIES = (
        "brevo",
        "brevo_e_commerce_get_all_categories",
        False,
    )
    BREVO_E_COMMERCE_CREATE_CATEGORY = (
        "brevo",
        "brevo_e_commerce_create_category",
        False,
    )
    BREVO_E_COMMERCE_GET_CATEGORY_DETAILS = (
        "brevo",
        "brevo_e_commerce_get_category_details",
        False,
    )
    BREVO_E_COMMERCE_CREATE_CATEGORIES_BATCH = (
        "brevo",
        "brevo_e_commerce_create_categories_batch",
        False,
    )
    BREVO_E_COMMERCE_LIST_ALL_PRODUCTS = (
        "brevo",
        "brevo_e_commerce_list_all_products",
        False,
    )
    BREVO_E_COMMERCE_CREATE_PRODUCT = (
        "brevo",
        "brevo_e_commerce_create_product",
        False,
    )
    BREVO_E_COMMERCE_GET_PRODUCT_DETAILS = (
        "brevo",
        "brevo_e_commerce_get_product_details",
        False,
    )
    BREVO_E_COMMERCE_CREATE_PRODUCTS_BATCH = (
        "brevo",
        "brevo_e_commerce_create_products_batch",
        False,
    )
    BREVO_COUPONS_LIST_COUPON_COLLECTIONS = (
        "brevo",
        "brevo_coupons_list_coupon_collections",
        False,
    )
    BREVO_COUPONS_CREATE_COLLECTION = (
        "brevo",
        "brevo_coupons_create_collection",
        False,
    )
    BREVO_COUPONS_GET_BY_ID = ("brevo", "brevo_coupons_get_by_id", False)
    BREVO_COUPONS_UPDATE_COUPON_COLLECTION_BY_ID = (
        "brevo",
        "brevo_coupons_update_coupon_collection_by_id",
        False,
    )
    BREVO_COUPONS_CREATE_COUPON_COLLECTION = (
        "brevo",
        "brevo_coupons_create_coupon_collection",
        False,
    )
    BREVO_TRANSACTIONAL_WHATS_APPS_END_MESSAGE = (
        "brevo",
        "brevo_transactional_whats_apps_end_message",
        False,
    )
    BREVO_TRANSACTIONAL_WHATS_APP_GET_ACTIVITY = (
        "brevo",
        "brevo_transactional_whats_app_get_activity",
        False,
    )
    BREVO_EXTERNAL_FEEDS_GET_ALL_FEEDS = (
        "brevo",
        "brevo_external_feeds_get_all_feeds",
        False,
    )
    BREVO_EXTERNAL_FEEDS_CREATE_FEED = (
        "brevo",
        "brevo_external_feeds_create_feed",
        False,
    )
    BREVO_EXTERNAL_FEEDS_GET_FEED_BYUU_ID = (
        "brevo",
        "brevo_external_feeds_get_feed_byuu_id",
        False,
    )
    BREVO_EXTERNAL_FEEDS_UPDATE_FEED_BYUU_ID = (
        "brevo",
        "brevo_external_feeds_update_feed_byuu_id",
        False,
    )
    BREVO_EXTERNAL_FEEDS_DELETE_FEED_BYUU_ID = (
        "brevo",
        "brevo_external_feeds_delete_feed_byuu_id",
        False,
    )
    ATTIO_LIST_OBJECTS = ("attio", "attio_list_objects", False)
    ATTIO_CREATE_AN_OBJECT = ("attio", "attio_create_an_object", False)
    ATTIO_GET_AN_OBJECT = ("attio", "attio_get_an_object", False)
    ATTIO_UPDATE_AN_OBJECT = ("attio", "attio_update_an_object", False)
    ATTIO_LIST_ATTRIBUTES = ("attio", "attio_list_attributes", False)
    ATTIO_CREATE_AN_ATTRIBUTE = ("attio", "attio_create_an_attribute", False)
    ATTIO_GET_AN_ATTRIBUTE = ("attio", "attio_get_an_attribute", False)
    ATTIO_UPDATE_AN_ATTRIBUTE = ("attio", "attio_update_an_attribute", False)
    ATTIO_LIST_SELECT_OPTIONS = ("attio", "attio_list_select_options", False)
    ATTIO_CREATEA_SELECT_OPTION = ("attio", "attio_createa_select_option", False)
    ATTIO_UPDATEA_SELECT_OPTION = ("attio", "attio_updatea_select_option", False)
    ATTIO_LIST_STATUSES = ("attio", "attio_list_statuses", False)
    ATTIO_CREATEA_STATUS = ("attio", "attio_createa_status", False)
    ATTIO_UPDATEA_STATUS = ("attio", "attio_updatea_status", False)
    ATTIO_LIST_RECORDS = ("attio", "attio_list_records", False)
    ATTIO_CREATEA_RECORD = ("attio", "attio_createa_record", False)
    ATTIO_ASSERTA_RECORD = ("attio", "attio_asserta_record", False)
    ATTIO_GETA_RECORD = ("attio", "attio_geta_record", False)
    ATTIO_UPDATEA_RECORD = ("attio", "attio_updatea_record", False)
    ATTIO_DELETEA_RECORD = ("attio", "attio_deletea_record", False)
    ATTIO_LIST_RECORD_ATTRIBUTE_VALUES = (
        "attio",
        "attio_list_record_attribute_values",
        False,
    )
    ATTIO_LIST_RECORD_ENTRIES = ("attio", "attio_list_record_entries", False)
    ATTIO_LIST_ALL_LISTS = ("attio", "attio_list_all_lists", False)
    ATTIO_CREATEA_LIST = ("attio", "attio_createa_list", False)
    ATTIO_GETA_LIST = ("attio", "attio_geta_list", False)
    ATTIO_UPDATEA_LIST = ("attio", "attio_updatea_list", False)
    ATTIO_LIST_ENTRIES = ("attio", "attio_list_entries", False)
    ATTIO_CREATE_AN_ENTRY_ADD_RECORD_TO_LIST = (
        "attio",
        "attio_create_an_entry_add_record_to_list",
        False,
    )
    ATTIO_ASSERTA_LIST_ENTRY_BY_PARENT = (
        "attio",
        "attio_asserta_list_entry_by_parent",
        False,
    )
    ATTIO_GETA_LIST_ENTRY = ("attio", "attio_geta_list_entry", False)
    ATTIO_UPDATEA_LIST_ENTRY_APPEND_MULTI_SELECT_VALUES = (
        "attio",
        "attio_updatea_list_entry_append_multi_select_values",
        False,
    )
    ATTIO_UPDATEA_LIST_ENTRY_OVERWRITE_MULTI_SELECT_VALUES = (
        "attio",
        "attio_updatea_list_entry_overwrite_multi_select_values",
        False,
    )
    ATTIO_DELETEA_LIST_ENTRY = ("attio", "attio_deletea_list_entry", False)
    ATTIO_LIST_ATTRIBUTE_VALUES_FORA_LIST_ENTRY = (
        "attio",
        "attio_list_attribute_values_fora_list_entry",
        False,
    )
    ATTIO_LIST_WORK_SPACE_MEMBERS = ("attio", "attio_list_work_space_members", False)
    ATTIO_GETA_WORK_SPACE_MEMBER = ("attio", "attio_geta_work_space_member", False)
    ATTIO_LIST_NOTES = ("attio", "attio_list_notes", False)
    ATTIO_CREATEA_NOTE = ("attio", "attio_createa_note", False)
    ATTIO_GETA_NOTE = ("attio", "attio_geta_note", False)
    ATTIO_DELETEA_NOTE = ("attio", "attio_deletea_note", False)
    ATTIO_LIST_TASKS = ("attio", "attio_list_tasks", False)
    ATTIO_CREATEA_TASK = ("attio", "attio_createa_task", False)
    ATTIO_GETA_TASK = ("attio", "attio_geta_task", False)
    ATTIO_UPDATEA_TASK = ("attio", "attio_updatea_task", False)
    ATTIO_DELETEA_TASK = ("attio", "attio_deletea_task", False)
    ATTIO_LIST_THREADS = ("attio", "attio_list_threads", False)
    ATTIO_GETA_THREAD = ("attio", "attio_geta_thread", False)
    ATTIO_CREATEA_COMMENT = ("attio", "attio_createa_comment", False)
    ATTIO_GETA_COMMENT = ("attio", "attio_geta_comment", False)
    ATTIO_DELETEA_COMMENT = ("attio", "attio_deletea_comment", False)
    ATTIO_LIST_WEB_HOOKS = ("attio", "attio_list_web_hooks", False)
    ATTIO_CREATEA_WEB_HOOK = ("attio", "attio_createa_web_hook", False)
    ATTIO_GETA_WEB_HOOK = ("attio", "attio_geta_web_hook", False)
    ATTIO_UPDATEA_WEB_HOOK = ("attio", "attio_updatea_web_hook", False)
    ATTIO_DELETEA_WEB_HOOK = ("attio", "attio_deletea_web_hook", False)
    ATTIO_IDENTIFY = ("attio", "attio_identify", False)
    GITHUB_CREATE_ISSUE = ("github", "github_create_issue", False)
    GITHUB_LIST_GITHUB_REPOS = ("github", "github_list_github_repos", False)
    GITHUB_STAR_REPO = ("github", "github_star_repo", False)
    GITHUB_GET_ABOUT_ME = ("github", "github_get_about_me", False)
    GITHUB_FETCH_README = ("github", "github_fetch_readme", False)
    GITHUB_GET_COMMITS = ("github", "github_get_commits", False)
    GITHUB_GET_COMMITS_WITH_CODE = ("github", "github_get_commits_with_code", False)
    GITHUB_GET_PATCH_FOR_COMMIT = ("github", "github_get_patch_for_commit", False)
    LINEAR_CREATE_LINEAR_ISSUE = ("linear", "linear_create_linear_issue", False)
    LINEAR_LIST_LINEAR_PROJECTS = ("linear", "linear_list_linear_projects", False)
    LINEAR_LIST_LINEAR_TEAMS = ("linear", "linear_list_linear_teams", False)
    ASANA_ALLOCATIONS_GET_RECORD_BY_ID = (
        "asana",
        "asana_allocations_get_record_by_id",
        False,
    )
    ASANA_ALLOCATIONS_UPDATE_RECORD_BY_ID = (
        "asana",
        "asana_allocations_update_record_by_id",
        False,
    )
    ASANA_ALLOCATIONS_DELETE_ALLOCATION_BY_ID = (
        "asana",
        "asana_allocations_delete_allocation_by_id",
        False,
    )
    ASANA_ALLOCATIONS_GET_MULTIPLE = ("asana", "asana_allocations_get_multiple", False)
    ASANA_ALLOCATIONS_CREATE_RECORD = (
        "asana",
        "asana_allocations_create_record",
        False,
    )
    ASANA_ATTACHMENTS_GET_ATTACHMENT_RECORD = (
        "asana",
        "asana_attachments_get_attachment_record",
        False,
    )
    ASANA_ATTACHMENTS_DELETE_SPECIFIC = (
        "asana",
        "asana_attachments_delete_specific",
        False,
    )
    ASANA_ATTACHMENTS_GET_ALL_FOR_OBJECT = (
        "asana",
        "asana_attachments_get_all_for_object",
        False,
    )
    ASANA_ATTACHMENTS_UPLOAD_ATTACHMENT = (
        "asana",
        "asana_attachments_upload_attachment",
        False,
    )
    ASANA_AUDIT_LOG_API_GET_AUDIT_LOG_EVENTS = (
        "asana",
        "asana_audit_log_api_get_audit_log_events",
        False,
    )
    ASANA_BATCH_API_SUBMIT_PARALLEL_REQUESTS = (
        "asana",
        "asana_batch_api_submit_parallel_requests",
        False,
    )
    ASANA_CUSTOM_FIELD_SETTINGS_GET_PROJECT_CUSTOM_FIELD_SETTINGS = (
        "asana",
        "asana_custom_field_settings_get_project_custom_field_settings",
        False,
    )
    ASANA_CUSTOM_FIELD_SETTINGS_GET_PORTFOLIO_CUSTOM_FIELD_SETTINGS = (
        "asana",
        "asana_custom_field_settings_get_portfolio_custom_field_settings",
        False,
    )
    ASANA_CUSTOM_FIELDS_CREATE_NEW_FIELD_RECORD = (
        "asana",
        "asana_custom_fields_create_new_field_record",
        False,
    )
    ASANA_CUSTOM_FIELDS_GET_METADATA = (
        "asana",
        "asana_custom_fields_get_metadata",
        False,
    )
    ASANA_CUSTOM_FIELDS_UPDATE_FIELD_RECORD = (
        "asana",
        "asana_custom_fields_update_field_record",
        False,
    )
    ASANA_CUSTOM_FIELDS_DELETE_FIELD_RECORD = (
        "asana",
        "asana_custom_fields_delete_field_record",
        False,
    )
    ASANA_CUSTOM_FIELDS_LIST_WORK_SPACE_CUSTOM_FIELDS = (
        "asana",
        "asana_custom_fields_list_work_space_custom_fields",
        False,
    )
    ASANA_CUSTOM_FIELDS_ADDE_NUM_OPTION = (
        "asana",
        "asana_custom_fields_adde_num_option",
        False,
    )
    ASANA_CUSTOM_FIELDS_REORDERE_NUM_OPTION = (
        "asana",
        "asana_custom_fields_reordere_num_option",
        False,
    )
    ASANA_CUSTOM_FIELDS_UPDATEE_NUM_OPTION = (
        "asana",
        "asana_custom_fields_updatee_num_option",
        False,
    )
    ASANA_EVENTS_GET_RESOURCE_EVENTS = (
        "asana",
        "asana_events_get_resource_events",
        False,
    )
    ASANA_GOAL_RELATIONSHIPS_GET_RECORD_BY_ID = (
        "asana",
        "asana_goal_relationships_get_record_by_id",
        False,
    )
    ASANA_GOAL_RELATIONSHIPS_UPDATE_GOAL_RELATIONSHIP_RECORD = (
        "asana",
        "asana_goal_relationships_update_goal_relationship_record",
        False,
    )
    ASANA_GOAL_RELATIONSHIPS_GET_COMPACT_RECORDS = (
        "asana",
        "asana_goal_relationships_get_compact_records",
        False,
    )
    ASANA_GOAL_RELATIONSHIPS_CREATE_SUPPORTING_RELATIONSHIP = (
        "asana",
        "asana_goal_relationships_create_supporting_relationship",
        False,
    )
    ASANA_GOAL_RELATIONSHIPS_REMOVE_SUPPORTING_RELATIONSHIP = (
        "asana",
        "asana_goal_relationships_remove_supporting_relationship",
        False,
    )
    ASANA_GOALS_GET_GOAL_RECORD = ("asana", "asana_goals_get_goal_record", False)
    ASANA_GOALS_UPDATE_GOAL_RECORD = ("asana", "asana_goals_update_goal_record", False)
    ASANA_GOALS_DELETE_RECORD = ("asana", "asana_goals_delete_record", False)
    ASANA_GOALS_GET_COMPACT_RECORDS = (
        "asana",
        "asana_goals_get_compact_records",
        False,
    )
    ASANA_GOALS_CREATE_NEW_GOAL_RECORD = (
        "asana",
        "asana_goals_create_new_goal_record",
        False,
    )
    ASANA_GOALS_CREATE_METRIC = ("asana", "asana_goals_create_metric", False)
    ASANA_GOALS_UPDATE_METRIC_CURRENT_VALUE = (
        "asana",
        "asana_goals_update_metric_current_value",
        False,
    )
    ASANA_GOALS_ADD_COLLABORATORS_TO_GOAL = (
        "asana",
        "asana_goals_add_collaborators_to_goal",
        False,
    )
    ASANA_GOALS_REMOVE_FOLLOWERS_FROM_GOAL = (
        "asana",
        "asana_goals_remove_followers_from_goal",
        False,
    )
    ASANA_GOALS_GET_PARENT_GOALS = ("asana", "asana_goals_get_parent_goals", False)
    ASANA_JOBS_GET_BY_ID = ("asana", "asana_jobs_get_by_id", False)
    ASANA_MEMBERSHIPS_GET_MULTIPLE = ("asana", "asana_memberships_get_multiple", False)
    ASANA_MEMBERSHIPS_CREATE_NEW_RECORD = (
        "asana",
        "asana_memberships_create_new_record",
        False,
    )
    ASANA_MEMBERSHIPS_GET_MEMBERSHIP_RECORD = (
        "asana",
        "asana_memberships_get_membership_record",
        False,
    )
    ASANA_MEMBERSHIPS_UPDATE_MEMBERSHIP_RECORD = (
        "asana",
        "asana_memberships_update_membership_record",
        False,
    )
    ASANA_MEMBERSHIPS_DELETE_RECORD = (
        "asana",
        "asana_memberships_delete_record",
        False,
    )
    ASANA_ORGANIZATION_EXPORTS_CREATE_EXPORT_REQUEST = (
        "asana",
        "asana_organization_exports_create_export_request",
        False,
    )
    ASANA_ORGANIZATION_EXPORTS_GET_EXPORT_DETAILS = (
        "asana",
        "asana_organization_exports_get_export_details",
        False,
    )
    ASANA_PORTFOLIO_MEMBERSHIPS_LIST_MULTIPLE_MEMBERSHIPS = (
        "asana",
        "asana_portfolio_memberships_list_multiple_memberships",
        False,
    )
    ASANA_PORTFOLIO_MEMBERSHIPS_GET_COMPLETE_RECORD = (
        "asana",
        "asana_portfolio_memberships_get_complete_record",
        False,
    )
    ASANA_PORTFOLIO_MEMBERSHIPS_GET_COMPACT = (
        "asana",
        "asana_portfolio_memberships_get_compact",
        False,
    )
    ASANA_PORTFOLIOS_LIST_MULTIPLE_PORTFOLIOS = (
        "asana",
        "asana_portfolios_list_multiple_portfolios",
        False,
    )
    ASANA_PORTFOLIOS_CREATE_NEW_PORTFOLIO_RECORD = (
        "asana",
        "asana_portfolios_create_new_portfolio_record",
        False,
    )
    ASANA_PORTFOLIOS_GET_RECORD = ("asana", "asana_portfolios_get_record", False)
    ASANA_PORTFOLIOS_UPDATE_PORTFOLIO_RECORD = (
        "asana",
        "asana_portfolios_update_portfolio_record",
        False,
    )
    ASANA_PORTFOLIOS_DELETE_RECORD = ("asana", "asana_portfolios_delete_record", False)
    ASANA_PORTFOLIOS_GET_ITEMS = ("asana", "asana_portfolios_get_items", False)
    ASANA_PORTFOLIOS_ADD_PORTFOLIO_ITEM = (
        "asana",
        "asana_portfolios_add_portfolio_item",
        False,
    )
    ASANA_PORTFOLIOS_REMOVE_ITEM_FROM_PORTFOLIO = (
        "asana",
        "asana_portfolios_remove_item_from_portfolio",
        False,
    )
    ASANA_PORTFOLIOS_ADD_CUSTOM_FIELD_SETTING = (
        "asana",
        "asana_portfolios_add_custom_field_setting",
        False,
    )
    ASANA_PORTFOLIOS_REMOVE_CUSTOM_FIELD_SETTING = (
        "asana",
        "asana_portfolios_remove_custom_field_setting",
        False,
    )
    ASANA_PORTFOLIOS_ADD_MEMBERS_TO_PORTFOLIO = (
        "asana",
        "asana_portfolios_add_members_to_portfolio",
        False,
    )
    ASANA_PORTFOLIOS_REMOVE_MEMBERS_FROM_PORTFOLIO = (
        "asana",
        "asana_portfolios_remove_members_from_portfolio",
        False,
    )
    ASANA_PROJECT_BRIEFS_GET_FULL_RECORD = (
        "asana",
        "asana_project_briefs_get_full_record",
        False,
    )
    ASANA_PROJECT_BRIEFS_UPDATE_BRIEF_RECORD = (
        "asana",
        "asana_project_briefs_update_brief_record",
        False,
    )
    ASANA_PROJECT_BRIEFS_REMOVE_BRIEF = (
        "asana",
        "asana_project_briefs_remove_brief",
        False,
    )
    ASANA_PROJECT_BRIEFS_CREATE_NEW_RECORD = (
        "asana",
        "asana_project_briefs_create_new_record",
        False,
    )
    ASANA_PROJECT_MEMBERSHIPS_GET_RECORD = (
        "asana",
        "asana_project_memberships_get_record",
        False,
    )
    ASANA_PROJECT_MEMBERSHIPS_GET_COMPACT_RECORDS = (
        "asana",
        "asana_project_memberships_get_compact_records",
        False,
    )
    ASANA_PROJECT_STATUSES_GET_STATUS_UPDATE_RECORD = (
        "asana",
        "asana_project_statuses_get_status_update_record",
        False,
    )
    ASANA_PROJECT_STATUSES_DELETE_SPECIFIC_STATUS_UPDATE = (
        "asana",
        "asana_project_statuses_delete_specific_status_update",
        False,
    )
    ASANA_PROJECT_STATUSES_GET_PROJECT_UPDATES = (
        "asana",
        "asana_project_statuses_get_project_updates",
        False,
    )
    ASANA_PROJECT_STATUSES_CREATE_NEW_STATUS_UPDATE_RECORD = (
        "asana",
        "asana_project_statuses_create_new_status_update_record",
        False,
    )
    ASANA_PROJECT_TEMPLATES_GET_RECORD = (
        "asana",
        "asana_project_templates_get_record",
        False,
    )
    ASANA_PROJECT_TEMPLATES_DELETE_TEMPLATE_RECORD = (
        "asana",
        "asana_project_templates_delete_template_record",
        False,
    )
    ASANA_PROJECT_TEMPLATES_LIST_MULTIPLE = (
        "asana",
        "asana_project_templates_list_multiple",
        False,
    )
    ASANA_PROJECT_TEMPLATES_GET_ALL_TEMPLATE_RECORDS = (
        "asana",
        "asana_project_templates_get_all_template_records",
        False,
    )
    ASANA_PROJECT_TEMPLATES_INSTANTIATE_PROJECT_JOB = (
        "asana",
        "asana_project_templates_instantiate_project_job",
        False,
    )
    ASANA_PROJECTS_LIST_MULTIPLE = ("asana", "asana_projects_list_multiple", False)
    ASANA_PROJECTS_CREATE_NEW_PROJECT_RECORD = (
        "asana",
        "asana_projects_create_new_project_record",
        False,
    )
    ASANA_PROJECTS_GET_PROJECT_RECORD = (
        "asana",
        "asana_projects_get_project_record",
        False,
    )
    ASANA_PROJECTS_UPDATE_PROJECT_RECORD = (
        "asana",
        "asana_projects_update_project_record",
        False,
    )
    ASANA_PROJECTS_DELETE_PROJECT_BY_ID = (
        "asana",
        "asana_projects_delete_project_by_id",
        False,
    )
    ASANA_PROJECTS_DUPLICATE_PROJECT_JOB = (
        "asana",
        "asana_projects_duplicate_project_job",
        False,
    )
    ASANA_PROJECTS_TASK_PROJECTS_LIST = (
        "asana",
        "asana_projects_task_projects_list",
        False,
    )
    ASANA_PROJECTS_GET_TEAM_PROJECTS = (
        "asana",
        "asana_projects_get_team_projects",
        False,
    )
    ASANA_PROJECTS_CREATE_PROJECT_FOR_TEAM = (
        "asana",
        "asana_projects_create_project_for_team",
        False,
    )
    ASANA_PROJECTS_GET_ALL_IN_WORK_SPACE = (
        "asana",
        "asana_projects_get_all_in_work_space",
        False,
    )
    ASANA_PROJECTS_CREATE_IN_WORK_SPACE = (
        "asana",
        "asana_projects_create_in_work_space",
        False,
    )
    ASANA_PROJECTS_ADD_CUSTOM_FIELD_SETTING = (
        "asana",
        "asana_projects_add_custom_field_setting",
        False,
    )
    ASANA_PROJECTS_REMOVE_CUSTOM_FIELD = (
        "asana",
        "asana_projects_remove_custom_field",
        False,
    )
    ASANA_PROJECTS_GET_TASK_COUNTS = ("asana", "asana_projects_get_task_counts", False)
    ASANA_PROJECTS_ADD_MEMBERS_TO_PROJECT = (
        "asana",
        "asana_projects_add_members_to_project",
        False,
    )
    ASANA_PROJECTS_REMOVE_MEMBERS_FROM_PROJECT = (
        "asana",
        "asana_projects_remove_members_from_project",
        False,
    )
    ASANA_PROJECTS_ADD_FOLLOWERS_TO_PROJECT = (
        "asana",
        "asana_projects_add_followers_to_project",
        False,
    )
    ASANA_PROJECTS_REMOVE_PROJECT_FOLLOWERS = (
        "asana",
        "asana_projects_remove_project_followers",
        False,
    )
    ASANA_PROJECTS_CREATE_PROJECT_TEMPLATE_JOB = (
        "asana",
        "asana_projects_create_project_template_job",
        False,
    )
    ASANA_RULES_TRIGGER_RULE_REQUEST = (
        "asana",
        "asana_rules_trigger_rule_request",
        False,
    )
    ASANA_SECTIONS_GET_RECORD = ("asana", "asana_sections_get_record", False)
    ASANA_SECTIONS_UPDATE_SECTION_RECORD = (
        "asana",
        "asana_sections_update_section_record",
        False,
    )
    ASANA_SECTIONS_DELETE_SECTION = ("asana", "asana_sections_delete_section", False)
    ASANA_SECTIONS_LIST_PROJECT_SECTIONS = (
        "asana",
        "asana_sections_list_project_sections",
        False,
    )
    ASANA_SECTIONS_CREATE_NEW_SECTION = (
        "asana",
        "asana_sections_create_new_section",
        False,
    )
    ASANA_SECTIONS_ADD_TASK_TO_SECTION = (
        "asana",
        "asana_sections_add_task_to_section",
        False,
    )
    ASANA_SECTIONS_MOVE_OR_INSERT = ("asana", "asana_sections_move_or_insert", False)
    ASANA_STATUS_UPDATES_GET_RECORD_BY_ID = (
        "asana",
        "asana_status_updates_get_record_by_id",
        False,
    )
    ASANA_STATUS_UPDATES_DELETE_SPECIFIC_STATUS_UPDATE = (
        "asana",
        "asana_status_updates_delete_specific_status_update",
        False,
    )
    ASANA_STATUS_UPDATES_GET_COMPACT_RECORDS = (
        "asana",
        "asana_status_updates_get_compact_records",
        False,
    )
    ASANA_STATUS_UPDATES_CREATE_NEW_STATUS_UPDATE_RECORD = (
        "asana",
        "asana_status_updates_create_new_status_update_record",
        False,
    )
    ASANA_STORIES_GET_FULL_RECORD = ("asana", "asana_stories_get_full_record", False)
    ASANA_STORIES_UPDATE_FULL_RECORD = (
        "asana",
        "asana_stories_update_full_record",
        False,
    )
    ASANA_STORIES_DELETE_STORY_RECORD = (
        "asana",
        "asana_stories_delete_story_record",
        False,
    )
    ASANA_STORIES_GET_TASK_STORIES = ("asana", "asana_stories_get_task_stories", False)
    ASANA_STORIES_CREATE_COMMENT = ("asana", "asana_stories_create_comment", False)
    ASANA_TAGS_LIST_FILTERED_TAGS = ("asana", "asana_tags_list_filtered_tags", False)
    ASANA_TAGS_CREATE_NEW_TAG_RECORD = (
        "asana",
        "asana_tags_create_new_tag_record",
        False,
    )
    ASANA_TAGS_GET_RECORD = ("asana", "asana_tags_get_record", False)
    ASANA_TAGS_UPDATE_TAG_RECORD = ("asana", "asana_tags_update_tag_record", False)
    ASANA_TAGS_REMOVE_TAG = ("asana", "asana_tags_remove_tag", False)
    ASANA_TAGS_GET_TASK_TAGS = ("asana", "asana_tags_get_task_tags", False)
    ASANA_TAGS_GET_FILTERED_TAGS = ("asana", "asana_tags_get_filtered_tags", False)
    ASANA_TAGS_CREATE_TAG_IN_WORK_SPACE = (
        "asana",
        "asana_tags_create_tag_in_work_space",
        False,
    )
    ASANA_TASK_TEMPLATES_LIST_MULTIPLE = (
        "asana",
        "asana_task_templates_list_multiple",
        False,
    )
    ASANA_TASK_TEMPLATES_GET_SINGLE_TEMPLATE = (
        "asana",
        "asana_task_templates_get_single_template",
        False,
    )
    ASANA_TASK_TEMPLATES_DELETE_TASK_TEMPLATE = (
        "asana",
        "asana_task_templates_delete_task_template",
        False,
    )
    ASANA_TASK_TEMPLATES_INSTANTIATE_TASK_JOB = (
        "asana",
        "asana_task_templates_instantiate_task_job",
        False,
    )
    ASANA_TASKS_GET_MULTIPLE = ("asana", "asana_tasks_get_multiple", False)
    ASANA_TASKS_CREATE_NEW_TASK = ("asana", "asana_tasks_create_new_task", False)
    ASANA_TASKS_GET_TASK_RECORD = ("asana", "asana_tasks_get_task_record", False)
    ASANA_TASKS_UPDATE_TASK_RECORD = ("asana", "asana_tasks_update_task_record", False)
    ASANA_TASKS_DELETE_TASK = ("asana", "asana_tasks_delete_task", False)
    ASANA_TASKS_DUPLICATE_TASK_JOB = ("asana", "asana_tasks_duplicate_task_job", False)
    ASANA_TASKS_GET_TASKS_BY_PROJECT = (
        "asana",
        "asana_tasks_get_tasks_by_project",
        False,
    )
    ASANA_TASKS_GET_SECTION_TASKS = ("asana", "asana_tasks_get_section_tasks", False)
    ASANA_TASKS_GET_MULTIPLE_WITH_TAG = (
        "asana",
        "asana_tasks_get_multiple_with_tag",
        False,
    )
    ASANA_TASKS_GET_USER_TASK_LIST_TASKS = (
        "asana",
        "asana_tasks_get_user_task_list_tasks",
        False,
    )
    ASANA_TASKS_GET_SUB_TASK_LIST = ("asana", "asana_tasks_get_sub_task_list", False)
    ASANA_TASKS_CREATE_SUB_TASK_RECORD = (
        "asana",
        "asana_tasks_create_sub_task_record",
        False,
    )
    ASANA_TASKS_SET_PARENT_TASK = ("asana", "asana_tasks_set_parent_task", False)
    ASANA_TASKS_GET_ALL_DEPENDENCIES = (
        "asana",
        "asana_tasks_get_all_dependencies",
        False,
    )
    ASANA_TASKS_SET_DEPENDENCIES_FOR_TASK = (
        "asana",
        "asana_tasks_set_dependencies_for_task",
        False,
    )
    ASANA_TASK_SUN_LINK_DEPENDENCIES_FROM_TASK = (
        "asana",
        "asana_task_sun_link_dependencies_from_task",
        False,
    )
    ASANA_TASKS_GET_DEPENDENTS = ("asana", "asana_tasks_get_dependents", False)
    ASANA_TASKS_SET_TASK_DEPENDENTS = (
        "asana",
        "asana_tasks_set_task_dependents",
        False,
    )
    ASANA_TASK_SUN_LINK_DEPENDENTS = ("asana", "asana_task_sun_link_dependents", False)
    ASANA_TASKS_ADD_PROJECT_TO_TASK = (
        "asana",
        "asana_tasks_add_project_to_task",
        False,
    )
    ASANA_TASKS_REMOVE_PROJECT_FROM_TASK = (
        "asana",
        "asana_tasks_remove_project_from_task",
        False,
    )
    ASANA_TASKS_ADD_TAG_TO_TASK = ("asana", "asana_tasks_add_tag_to_task", False)
    ASANA_TASKS_REMOVE_TAG_FROM_TASK = (
        "asana",
        "asana_tasks_remove_tag_from_task",
        False,
    )
    ASANA_TASKS_ADD_FOLLOWERS_TO_TASK = (
        "asana",
        "asana_tasks_add_followers_to_task",
        False,
    )
    ASANA_TASKS_REMOVE_FOLLOWERS_FROM_TASK = (
        "asana",
        "asana_tasks_remove_followers_from_task",
        False,
    )
    ASANA_TASKS_GET_BY_CUSTOM_ID = ("asana", "asana_tasks_get_by_custom_id", False)
    ASANA_TASKS_SEARCH_IN_WORK_SPACE = (
        "asana",
        "asana_tasks_search_in_work_space",
        False,
    )
    ASANA_TEAM_MEMBERSHIPS_GET_RECORD_BY_ID = (
        "asana",
        "asana_team_memberships_get_record_by_id",
        False,
    )
    ASANA_TEAM_MEMBERSHIPS_GET_COMPACT_RECORDS = (
        "asana",
        "asana_team_memberships_get_compact_records",
        False,
    )
    ASANA_TEAM_MEMBERSHIPS_GET_COMPACT = (
        "asana",
        "asana_team_memberships_get_compact",
        False,
    )
    ASANA_TEAM_MEMBERSHIPS_GET_USER_COMPACT = (
        "asana",
        "asana_team_memberships_get_user_compact",
        False,
    )
    ASANA_TEAMS_CREATE_TEAM_RECORD = ("asana", "asana_teams_create_team_record", False)
    ASANA_TEAMS_GET_TEAM_RECORD = ("asana", "asana_teams_get_team_record", False)
    ASANA_TEAMS_UPDATE_TEAM_RECORD = ("asana", "asana_teams_update_team_record", False)
    ASANA_TEAMS_LIST_WORK_SPACE_TEAMS = (
        "asana",
        "asana_teams_list_work_space_teams",
        False,
    )
    ASANA_TEAMS_GET_USER_TEAMS = ("asana", "asana_teams_get_user_teams", False)
    ASANA_TEAMS_ADD_USER_TO_TEAM = ("asana", "asana_teams_add_user_to_team", False)
    ASANA_TEAMS_REMOVE_USER_FROM_TEAM = (
        "asana",
        "asana_teams_remove_user_from_team",
        False,
    )
    ASANA_TIME_PERIODS_GET_FULL_RECORD = (
        "asana",
        "asana_time_periods_get_full_record",
        False,
    )
    ASANA_TIME_PERIODS_GET_COMPACT_TIME_PERIODS = (
        "asana",
        "asana_time_periods_get_compact_time_periods",
        False,
    )
    ASANA_TIME_TRACKING_ENTRIES_GET_FOR_TASK = (
        "asana",
        "asana_time_tracking_entries_get_for_task",
        False,
    )
    ASANA_TIME_TRACKING_ENTRIES_CREATE_NEW_TIME_ENTRY_RECORD = (
        "asana",
        "asana_time_tracking_entries_create_new_time_entry_record",
        False,
    )
    ASANA_TIME_TRACKING_ENTRIES_GET_RECORD = (
        "asana",
        "asana_time_tracking_entries_get_record",
        False,
    )
    ASANA_TIME_TRACKING_ENTRIES_UPDATE_TIME_TRACKING_ENTRY = (
        "asana",
        "asana_time_tracking_entries_update_time_tracking_entry",
        False,
    )
    ASANA_TIME_TRACKING_ENTRIES_DELETE_TIME_ENTRY = (
        "asana",
        "asana_time_tracking_entries_delete_time_entry",
        False,
    )
    ASANA_TYPE_AHEAD_GET_RESULTS = ("asana", "asana_type_ahead_get_results", False)
    ASANA_USER_TASK_LISTS_GET_RECORD = (
        "asana",
        "asana_user_task_lists_get_record",
        False,
    )
    ASANA_USER_TASK_LISTS_GET_USER_TASK_LIST = (
        "asana",
        "asana_user_task_lists_get_user_task_list",
        False,
    )
    ASANA_USERS_LIST_MULTIPLE_USERS = (
        "asana",
        "asana_users_list_multiple_users",
        False,
    )
    ASANA_USERS_GET_USER_RECORD = ("asana", "asana_users_get_user_record", False)
    ASANA_USERS_GET_FAVORITES_FOR_USER = (
        "asana",
        "asana_users_get_favorites_for_user",
        False,
    )
    ASANA_USERS_LIST_TEAM_USERS = ("asana", "asana_users_list_team_users", False)
    ASANA_USERS_LIST_WORK_SPACE_USERS = (
        "asana",
        "asana_users_list_work_space_users",
        False,
    )
    ASANA_WEB_HOOKS_LIST_MULTIPLE_WEB_HOOKS = (
        "asana",
        "asana_web_hooks_list_multiple_web_hooks",
        False,
    )
    ASANA_WEB_HOOKS_ESTABLISH_WEB_HOOK = (
        "asana",
        "asana_web_hooks_establish_web_hook",
        False,
    )
    ASANA_WEB_HOOKS_GET_WEB_HOOK_RECORD = (
        "asana",
        "asana_web_hooks_get_web_hook_record",
        False,
    )
    ASANA_WEB_HOOKS_UPDATE_WEB_HOOK_FILTERS = (
        "asana",
        "asana_web_hooks_update_web_hook_filters",
        False,
    )
    ASANA_WEB_HOOKS_REMOVE_WEB_HOOK = (
        "asana",
        "asana_web_hooks_remove_web_hook",
        False,
    )
    ASANA_WORK_SPACE_MEMBERSHIPS_GET_RECORD_BY_ID = (
        "asana",
        "asana_work_space_memberships_get_record_by_id",
        False,
    )
    ASANA_WORK_SPACE_MEMBERSHIPS_GET_USER_MEMBERSHIPS = (
        "asana",
        "asana_work_space_memberships_get_user_memberships",
        False,
    )
    ASANA_WORK_SPACE_MEMBERSHIPS_LIST_FOR_WORK_SPACE = (
        "asana",
        "asana_work_space_memberships_list_for_work_space",
        False,
    )
    ASANA_WORK_SPACES_LIST_MULTIPLE = (
        "asana",
        "asana_work_spaces_list_multiple",
        False,
    )
    ASANA_WORK_SPACES_GET_WORK_SPACE_RECORD = (
        "asana",
        "asana_work_spaces_get_work_space_record",
        False,
    )
    ASANA_WORK_SPACES_UPDATE_WORK_SPACE_RECORD = (
        "asana",
        "asana_work_spaces_update_work_space_record",
        False,
    )
    ASANA_WORK_SPACES_ADD_USER_TO_WORK_SPACE = (
        "asana",
        "asana_work_spaces_add_user_to_work_space",
        False,
    )
    ASANA_WORK_SPACES_REMOVE_USER_FROM_WORK_SPACE = (
        "asana",
        "asana_work_spaces_remove_user_from_work_space",
        False,
    )
    TRELLO_CREATE_TRELLO_LIST = ("trello", "trello_create_trello_list", False)
    TRELLO_CREATE_TRELLO_CARD = ("trello", "trello_create_trello_card", False)
    TRELLO_GET_TRELLO_BOARD_CARDS = ("trello", "trello_get_trello_board_cards", False)
    TRELLO_DELETE_TRELLO_CARD = ("trello", "trello_delete_trello_card", False)
    TRELLO_ADD_TRELLO_CARD_COMMENT = ("trello", "trello_add_trello_card_comment", False)
    TRELLO_CREATE_TRELLO_LABEL = ("trello", "trello_create_trello_label", False)
    TRELLO_UPDATE_TRELLO_BOARD = ("trello", "trello_update_trello_board", False)
    TRELLO_GET_ABOUT_ME = ("trello", "trello_get_about_me", False)
    TRELLO_SEARCH_TRELLO = ("trello", "trello_search_trello", False)
    TRELLO_SEARCH_TRELLO_MEMBER = ("trello", "trello_search_trello_member", False)
    TRELLO_UPDATE_TRELLO_CARD = ("trello", "trello_update_trello_card", False)
    TRELLO_GET_TRELLO_MEMBER_BOARD = ("trello", "trello_get_trello_member_board", False)
    NOTION_GET_ABOUT_ME = ("notion", "notion_get_about_me", False)
    NOTION_ADD_NOTION_PAGE_CHILDREN = (
        "notion",
        "notion_add_notion_page_children",
        False,
    )
    NOTION_ARCHIVE_NOTION_PAGE = ("notion", "notion_archive_notion_page", False)
    NOTION_CREATE_NOTION_DATABASE = ("notion", "notion_create_notion_database", False)
    NOTION_CREATE_PAGE_COMMENT = ("notion", "notion_create_page_comment", False)
    NOTION_CREATE_NOTION_PAGE = ("notion", "notion_create_notion_page", False)
    NOTION_DELETE_NOTION_PAGE_CHILDREN = (
        "notion",
        "notion_delete_notion_page_children",
        False,
    )
    NOTION_FETCH_NOTION_COMMENT = ("notion", "notion_fetch_notion_comment", False)
    NOTION_FETCH_NOTION_DATABASE = ("notion", "notion_fetch_notion_database", False)
    NOTION_FETCH_NOTION_PAGE = ("notion", "notion_fetch_notion_page", False)
    NOTION_SEARCH_NOTION_PAGE = ("notion", "notion_search_notion_page", False)
    NOTION_UPDATE_NOTION_DATABASE = ("notion", "notion_update_notion_database", False)
    NOTION_FETCH_NOTION_BLOCK = ("notion", "notion_fetch_notion_block", False)
    NOTION_FETCH_NOTION_CHILD_BLOCK = (
        "notion",
        "notion_fetch_notion_child_block",
        False,
    )
    TYPEFORM_GET_ABOUT_ME = ("typeform", "typeform_get_about_me", False)
    DROPBOX_GET_ABOUT_ME = ("dropbox", "dropbox_get_about_me", False)
    SLACK_SEND_SLACK_MESSAGE = ("slack", "slack_send_slack_message", False)
    SLACK_LIST_SLACK_CHANNELS = ("slack", "slack_list_slack_channels", False)
    SLACK_LIST_SLACK_MEMBERS = ("slack", "slack_list_slack_members", False)
    SLACK_LIST_SLACK_MESSAGES = ("slack", "slack_list_slack_messages", False)
    APIFY_LIST_APIFY_ACTORS = ("apify", "apify_list_apify_actors", False)
    APIFY_CREATE_APIFY_ACTOR = ("apify", "apify_create_apify_actor", False)
    APIFY_GET_ACTOR_ID = ("apify", "apify_get_actor_id", False)
    APIFY_SEARCH_STORE = ("apify", "apify_search_store", False)
    APIFY_GET_LAST_RUN_DATA = ("apify", "apify_get_last_run_data", False)
    APIFY_LIST_APIFY_TASKS = ("apify", "apify_list_apify_tasks", False)
    GMAIL_SEND_EMAIL = ("gmail", "gmail_send_email", False)
    GMAIL_CREATE_EMAIL_DRAFT = ("gmail", "gmail_create_email_draft", False)
    GMAIL_FIND_EMAIL_ID = ("gmail", "gmail_find_email_id", False)
    GMAIL_FETCH_LAST_THREE_MESSAGES = (
        "gmail",
        "gmail_fetch_last_three_messages",
        False,
    )
    GMAIL_ADD_LABEL_TO_EMAIL = ("gmail", "gmail_add_label_to_email", False)
    GMAIL_LIST_LABELS = ("gmail", "gmail_list_labels", False)
    GMAIL_FETCH_MESSAGE_BY_THREAD_ID = (
        "gmail",
        "gmail_fetch_message_by_thread_id",
        False,
    )
    GMAIL_REPLY_TO_THREAD = ("gmail", "gmail_reply_to_thread", False)
    GMAIL_FETCH_EMAILS_WITH_LABEL = ("gmail", "gmail_fetch_emails_with_label", False)
    SLACKBOT_SEND_SLACK_MESSAGE = ("slackbot", "slackbot_send_slack_message", False)
    SLACKBOT_LIST_SLACK_CHANNELS = ("slackbot", "slackbot_list_slack_channels", False)
    SLACKBOT_LIST_SLACK_MEMBERS = ("slackbot", "slackbot_list_slack_members", False)
    SLACKBOT_LIST_SLACK_MESSAGES = ("slackbot", "slackbot_list_slack_messages", False)
    CODEINTERPRETER_EXECUTE_CODE = (
        "codeinterpreter",
        "codeinterpreter_execute_code",
        True,
    )
    SERPAPI_SEARCH = ("serpapi", "serpapi_search", True)
    SNOWFLAKE_RUN_QUERY = ("snowflake", "snowflake_run_query", False)
    SNOWFLAKE_SHOW_TABLES = ("snowflake", "snowflake_show_tables", False)
    SNOWFLAKE_DESCRIBE_TABLE = ("snowflake", "snowflake_describe_table", False)
    SNOWFLAKE_EXPLORE_COLUMNS = ("snowflake", "snowflake_explore_columns", False)
    OKTA_APPLICATION_LIST_APPS = ("okta", "okta_application_list_apps", False)
    OKTA_APPLICATION_CREATE_NEW = ("okta", "okta_application_create_new", False)
    OKTA_APPLICATION_REMOVE_INACTIVE = (
        "okta",
        "okta_application_remove_inactive",
        False,
    )
    OKTA_APPLICATION_GET_BY_ID = ("okta", "okta_application_get_by_id", False)
    OKTA_APPLICATION_UPDATE_APPLICATION_IN_ORG = (
        "okta",
        "okta_application_update_application_in_org",
        False,
    )
    OKTA_APPLICATION_GET_DEFAULT_PROVISIONING_CONNECTION = (
        "okta",
        "okta_application_get_default_provisioning_connection",
        False,
    )
    OKTA_APPLICATION_SET_DEFAULT_PROVISIONING_CONNECTION = (
        "okta",
        "okta_application_set_default_provisioning_connection",
        False,
    )
    OKTA_APPLICATION_ACTIVATE_DEFAULT_PROVISIONING_CONNECTION = (
        "okta",
        "okta_application_activate_default_provisioning_connection",
        False,
    )
    OKTA_APPLICATION_DEACTIVATE_DEFAULT_PROVISIONING_CONNECTION = (
        "okta",
        "okta_application_deactivate_default_provisioning_connection",
        False,
    )
    OKTA_APPLICATION_LIST_CSRS_FOR_APPLICATION = (
        "okta",
        "okta_application_list_csrs_for_application",
        False,
    )
    OKTA_APPLICATION_GENERATE_CSR_FOR_APPLICATION = (
        "okta",
        "okta_application_generate_csr_for_application",
        False,
    )
    OKTA_APPLICATION_DELETE_CSR_BY_ID = (
        "okta",
        "okta_application_delete_csr_by_id",
        False,
    )
    OKTA_APPLICATION_GET_CREDENTIALS_CSRS = (
        "okta",
        "okta_application_get_credentials_csrs",
        False,
    )
    OKTA_APPLICATION_PUBLISH_CSR_LIFECYCLE = (
        "okta",
        "okta_application_publish_csr_lifecycle",
        False,
    )
    OKTA_APPLICATION_LIST_KEY_CREDENTIALS = (
        "okta",
        "okta_application_list_key_credentials",
        False,
    )
    OKTA_APPLICATION_GENERATEX509_CERTIFICATE = (
        "okta",
        "okta_application_generatex509_certificate",
        False,
    )
    OKTA_APPLICATION_GET_KEY_CREDENTIAL = (
        "okta",
        "okta_application_get_key_credential",
        False,
    )
    OKTA_APPLICATION_CLONE_APPLICATION_KEY_CREDENTIAL = (
        "okta",
        "okta_application_clone_application_key_credential",
        False,
    )
    OKTA_APPLICATION_LIST_CLIENT_SECRETS = (
        "okta",
        "okta_application_list_client_secrets",
        False,
    )
    OKTA_APPLICATION_ADD_CLIENT_SECRET = (
        "okta",
        "okta_application_add_client_secret",
        False,
    )
    OKTA_APPLICATION_REMOVE_SECRET = ("okta", "okta_application_remove_secret", False)
    OKTA_APPLICATION_GET_CLIENT_SECRET = (
        "okta",
        "okta_application_get_client_secret",
        False,
    )
    OKTA_APPLICATION_ACTIVATE_CLIENT_SECRET = (
        "okta",
        "okta_application_activate_client_secret",
        False,
    )
    OKTA_APPLICATION_DEACTIVATE_CLIENT_SECRET_BY_ID = (
        "okta",
        "okta_application_deactivate_client_secret_by_id",
        False,
    )
    OKTA_APPLICATION_LIST_FEATURES = ("okta", "okta_application_list_features", False)
    OKTA_APPLICATION_GET_FEATURE = ("okta", "okta_application_get_feature", False)
    OKTA_APPLICATION_UPDATE_FEATURE = ("okta", "okta_application_update_feature", False)
    OKTA_APPLICATION_LIST_SCOPE_CONSENT_GRANTS = (
        "okta",
        "okta_application_list_scope_consent_grants",
        False,
    )
    OKTA_APPLICATION_GRANT_CONSENT_TO_SCOPE = (
        "okta",
        "okta_application_grant_consent_to_scope",
        False,
    )
    OKTA_APPLICATION_REVOKE_PERMISSION = (
        "okta",
        "okta_application_revoke_permission",
        False,
    )
    OKTA_APPLICATION_GET_SINGLE_SCOPE_CONSENT_GRANT = (
        "okta",
        "okta_application_get_single_scope_consent_grant",
        False,
    )
    OKTA_APPLICATION_LIST_GROUPS_ASSIGNED = (
        "okta",
        "okta_application_list_groups_assigned",
        False,
    )
    OKTA_APPLICATION_REMOVE_GROUP_ASSIGNMENT = (
        "okta",
        "okta_application_remove_group_assignment",
        False,
    )
    OKTA_APPLICATION_GET_GROUP_ASSIGNMENT = (
        "okta",
        "okta_application_get_group_assignment",
        False,
    )
    OKTA_APPLICATION_ASSIGN_GROUP_TO = (
        "okta",
        "okta_application_assign_group_to",
        False,
    )
    OKTA_APPLICATION_ACTIVATE_INACTIVE = (
        "okta",
        "okta_application_activate_inactive",
        False,
    )
    OKTA_APPLICATION_DEACTIVATE_LIFECYCLE = (
        "okta",
        "okta_application_deactivate_lifecycle",
        False,
    )
    OKTA_APPLICATION_UPDATE_LOGO = ("okta", "okta_application_update_logo", False)
    OKTA_APPLICATION_ASSIGN_POLICY_TO_APPLICATION = (
        "okta",
        "okta_application_assign_policy_to_application",
        False,
    )
    OKTA_APPLICATION_PREVIEWS_AM_LAPP_METADATA = (
        "okta",
        "okta_application_previews_am_lapp_metadata",
        False,
    )
    OKTA_APPLICATION_REVOKE_ALL_TOKENS = (
        "okta",
        "okta_application_revoke_all_tokens",
        False,
    )
    OKTA_APPLICATION_LIST_TOKENS = ("okta", "okta_application_list_tokens", False)
    OKTA_APPLICATION_REVOKE_TOKEN = ("okta", "okta_application_revoke_token", False)
    OKTA_APPLICATION_GET_TOKEN = ("okta", "okta_application_get_token", False)
    OKTA_APPLICATION_LIST_ASSIGNED_USERS = (
        "okta",
        "okta_application_list_assigned_users",
        False,
    )
    OKTA_APPLICATION_ASSIGN_USER_TO_APPLICATION = (
        "okta",
        "okta_application_assign_user_to_application",
        False,
    )
    OKTA_APPLICATION_REMOVE_USER_FROM = (
        "okta",
        "okta_application_remove_user_from",
        False,
    )
    OKTA_APPLICATION_GET_SPECIFIC_USER_ASSIGNMENT = (
        "okta",
        "okta_application_get_specific_user_assignment",
        False,
    )
    OKTA_APPLICATION_UPDATE_PROFILE_FOR_USER = (
        "okta",
        "okta_application_update_profile_for_user",
        False,
    )
    OKTA_AUTHENTIC_AT_OR_LIST_ALL_AVAILABLE = (
        "okta",
        "okta_authentic_at_or_list_all_available",
        False,
    )
    OKTA_AUTHENTIC_AT_OR_CREATE_NEW = ("okta", "okta_authentic_at_or_create_new", False)
    OKTA_AUTHENTIC_AT_OR_GET_SUCCESS = (
        "okta",
        "okta_authentic_at_or_get_success",
        False,
    )
    OKTA_AUTHENTIC_AT_OR_UPDATE_AUTHENTIC_AT_OR = (
        "okta",
        "okta_authentic_at_or_update_authentic_at_or",
        False,
    )
    OKTA_AUTHENTIC_AT_OR_ACTIVATE_LIFECYCLE_SUCCESS = (
        "okta",
        "okta_authentic_at_or_activate_lifecycle_success",
        False,
    )
    OKTA_AUTHENTIC_AT_OR_DEACTIVATE_LIFECYCLE_SUCCESS = (
        "okta",
        "okta_authentic_at_or_deactivate_lifecycle_success",
        False,
    )
    OKTA_AUTHORIZATION_SERVER_LIST_SERVERS = (
        "okta",
        "okta_authorization_server_list_servers",
        False,
    )
    OKTA_AUTHORIZATION_SERVER_CREATE_NEW_SERVER = (
        "okta",
        "okta_authorization_server_create_new_server",
        False,
    )
    OKTA_AUTHORIZATION_SERVER_DELETE_SUCCESS = (
        "okta",
        "okta_authorization_server_delete_success",
        False,
    )
    OKTA_AUTHORIZATION_SERVER_GET_BY_ID = (
        "okta",
        "okta_authorization_server_get_by_id",
        False,
    )
    OKTA_AUTHORIZATION_SERVER_UPDATE_BY_ID = (
        "okta",
        "okta_authorization_server_update_by_id",
        False,
    )
    OKTA_AUTHORIZATION_SERVER_GET_CLAIMS = (
        "okta",
        "okta_authorization_server_get_claims",
        False,
    )
    OKTA_AUTHORIZATION_SERVER_CREATE_CLAIMS = (
        "okta",
        "okta_authorization_server_create_claims",
        False,
    )
    OKTA_AUTHORIZATION_SERVER_DELETE_CLAIM = (
        "okta",
        "okta_authorization_server_delete_claim",
        False,
    )
    OKTA_AUTHORIZATION_SERVER_GET_CLAIMS2 = (
        "okta",
        "okta_authorization_server_get_claims2",
        False,
    )
    OKTA_AUTHORIZATION_SERVER_UPDATE_CLAIM_SUCCESS = (
        "okta",
        "okta_authorization_server_update_claim_success",
        False,
    )
    OKTA_AUTHORIZATION_SERVER_LIST_CLIENTS = (
        "okta",
        "okta_authorization_server_list_clients",
        False,
    )
    OKTA_AUTHORIZATION_SERVER_DELETE_CLIENT_TOKEN = (
        "okta",
        "okta_authorization_server_delete_client_token",
        False,
    )
    OKTA_AUTHORIZATION_SERVER_GET_CLIENT_TOKENS = (
        "okta",
        "okta_authorization_server_get_client_tokens",
        False,
    )
    OKTA_AUTHORIZATION_SERVER_DELETE_AU_TH_TOKEN = (
        "okta",
        "okta_authorization_server_delete_au_th_token",
        False,
    )
    OKTA_AUTHORIZATION_SERVER_GET_CLIENT_AU_TH_TOKEN = (
        "okta",
        "okta_authorization_server_get_client_au_th_token",
        False,
    )
    OKTA_AUTHORIZATION_SERVER_LIST_CREDENTIALS_KEYS = (
        "okta",
        "okta_authorization_server_list_credentials_keys",
        False,
    )
    OKTA_AUTHORIZATION_SERVER_ROTATE_KEY_LIFECYCLE = (
        "okta",
        "okta_authorization_server_rotate_key_lifecycle",
        False,
    )
    OKTA_AUTHORIZATION_SERVER_ACTIVATE_LIFECYCLE_SUCCESS = (
        "okta",
        "okta_authorization_server_activate_lifecycle_success",
        False,
    )
    OKTA_AUTHORIZATION_SERVER_DEACTIVATE_LIFECYCLE = (
        "okta",
        "okta_authorization_server_deactivate_lifecycle",
        False,
    )
    OKTA_AUTHORIZATION_SERVER_GET_POLICIES_SUCCESS = (
        "okta",
        "okta_authorization_server_get_policies_success",
        False,
    )
    OKTA_AUTHORIZATION_SERVER_CREATE_POLICY = (
        "okta",
        "okta_authorization_server_create_policy",
        False,
    )
    OKTA_AUTHORIZATION_SERVER_DELETE_POLICY_BY_ID = (
        "okta",
        "okta_authorization_server_delete_policy_by_id",
        False,
    )
    OKTA_AUTHORIZATION_SERVER_GET_POLICIES = (
        "okta",
        "okta_authorization_server_get_policies",
        False,
    )
    OKTA_AUTHORIZATION_SERVER_UPDATE_POLICY_SUCCESS = (
        "okta",
        "okta_authorization_server_update_policy_success",
        False,
    )
    OKTA_AUTHORIZATION_SERVER_ACTIVATE_POLICY_LIFECYCLE = (
        "okta",
        "okta_authorization_server_activate_policy_lifecycle",
        False,
    )
    OKTA_AUTHORIZATION_SERVER_DEACTIVATE_POLICY_LIFECYCLE = (
        "okta",
        "okta_authorization_server_deactivate_policy_lifecycle",
        False,
    )
    OKTA_AUTHORIZATION_SERVER_ENUMERATE_POLICY_RULES = (
        "okta",
        "okta_authorization_server_enumerate_policy_rules",
        False,
    )
    OKTA_AUTHORIZATION_SERVER_CREATE_POLICY_RULE = (
        "okta",
        "okta_authorization_server_create_policy_rule",
        False,
    )
    OKTA_AUTHORIZATION_SERVER_DELETE_POLICY_RULE = (
        "okta",
        "okta_authorization_server_delete_policy_rule",
        False,
    )
    OKTA_AUTHORIZATION_SERVER_GET_POLICY_RULE_BY_ID = (
        "okta",
        "okta_authorization_server_get_policy_rule_by_id",
        False,
    )
    OKTA_AUTHORIZATION_SERVER_UPDATE_POLICY_RULE_CONFIGURATION = (
        "okta",
        "okta_authorization_server_update_policy_rule_configuration",
        False,
    )
    OKTA_AUTHORIZATION_SERVER_ACTIVATE_POLICY_RULE = (
        "okta",
        "okta_authorization_server_activate_policy_rule",
        False,
    )
    OKTA_AUTHORIZATION_SERVER_DEACTIVATE_POLICY_RULE = (
        "okta",
        "okta_authorization_server_deactivate_policy_rule",
        False,
    )
    OKTA_AUTHORIZATION_SERVER_GET_SCOPES = (
        "okta",
        "okta_authorization_server_get_scopes",
        False,
    )
    OKTA_AUTHORIZATION_SERVER_CREATE_SCOPE = (
        "okta",
        "okta_authorization_server_create_scope",
        False,
    )
    OKTA_AUTHORIZATION_SERVER_DELETE_SCOPE = (
        "okta",
        "okta_authorization_server_delete_scope",
        False,
    )
    OKTA_AUTHORIZATION_SERVER_GET_SCOPES2 = (
        "okta",
        "okta_authorization_server_get_scopes2",
        False,
    )
    OKTA_AUTHORIZATION_SERVER_UPDATE_SCOPE_SUCCESS = (
        "okta",
        "okta_authorization_server_update_scope_success",
        False,
    )
    OKTA_BRAND_GET_ALL_BRANDS = ("okta", "okta_brand_get_all_brands", False)
    OKTA_BRAND_GET_BY_ID = ("okta", "okta_brand_get_by_id", False)
    OKTA_BRAND_UPDATE_BY_BRAN_DID = ("okta", "okta_brand_update_by_bran_did", False)
    OKTA_BRAND_LIST_EMAIL_TEMPLATES = ("okta", "okta_brand_list_email_templates", False)
    OKTA_BRAND_GET_EMAIL_TEMPLATE = ("okta", "okta_brand_get_email_template", False)
    OKTA_BRAND_DELETE_EMAIL_TEMPLATE_CUSTOMIZATIONS = (
        "okta",
        "okta_brand_delete_email_template_customizations",
        False,
    )
    OKTA_BRAND_LIST_EMAIL_TEMPLATE_CUSTOMIZATIONS = (
        "okta",
        "okta_brand_list_email_template_customizations",
        False,
    )
    OKTA_BRAND_CREATE_EMAIL_TEMPLATE_CUSTOMIZATION = (
        "okta",
        "okta_brand_create_email_template_customization",
        False,
    )
    OKTA_BRAND_DELETE_EMAIL_CUSTOMIZATION = (
        "okta",
        "okta_brand_delete_email_customization",
        False,
    )
    OKTA_BRAND_GET_EMAIL_TEMPLATE_CUSTOMIZATION_BY_ID = (
        "okta",
        "okta_brand_get_email_template_customization_by_id",
        False,
    )
    OKTA_BRAND_UPDATE_EMAIL_CUSTOMIZATION = (
        "okta",
        "okta_brand_update_email_customization",
        False,
    )
    OKTA_BRAND_GET_EMAIL_CUSTOMIZATION_PREVIEW = (
        "okta",
        "okta_brand_get_email_customization_preview",
        False,
    )
    OKTA_BRAND_GET_EMAIL_TEMPLATE_DEFAULT_CONTENT = (
        "okta",
        "okta_brand_get_email_template_default_content",
        False,
    )
    OKTA_BRAND_GET_EMAIL_TEMPLATE_DEFAULT_CONTENT_PREVIEW = (
        "okta",
        "okta_brand_get_email_template_default_content_preview",
        False,
    )
    OKTA_BRAND_GET_EMAIL_TEMPLATE_DEFAULT_CONTENT_PREVIEW2 = (
        "okta",
        "okta_brand_get_email_template_default_content_preview2",
        False,
    )
    OKTA_BRAND_GET_THEMES = ("okta", "okta_brand_get_themes", False)
    OKTA_BRAND_GET_THEME_BY_ID = ("okta", "okta_brand_get_theme_by_id", False)
    OKTA_BRAND_UPDATE_THEME = ("okta", "okta_brand_update_theme", False)
    OKTA_BRAND_DELETE_THEME_BACKGROUND_IMAGE = (
        "okta",
        "okta_brand_delete_theme_background_image",
        False,
    )
    OKTA_BRAND_UPDATE_THEME_BACKGROUND_IMAGE = (
        "okta",
        "okta_brand_update_theme_background_image",
        False,
    )
    OKTA_BRAND_DELETE_THEME_FAVICON = ("okta", "okta_brand_delete_theme_favicon", False)
    OKTA_BRAND_UPDATE_THEME_FAVICON = ("okta", "okta_brand_update_theme_favicon", False)
    OKTA_BRAND_DELETE_THEME_LOGO = ("okta", "okta_brand_delete_theme_logo", False)
    OKTA_BRAND_UPDATE_THEME_LOGO = ("okta", "okta_brand_update_theme_logo", False)
    OKTA_DOMAIN_LIST_VERIFIED_CUSTOM = (
        "okta",
        "okta_domain_list_verified_custom",
        False,
    )
    OKTA_DOMAIN_CREATE_NEW_DOMAIN = ("okta", "okta_domain_create_new_domain", False)
    OKTA_DOMAIN_REMOVE_BY_ID = ("okta", "okta_domain_remove_by_id", False)
    OKTA_DOMAIN_GET_BY_ID = ("okta", "okta_domain_get_by_id", False)
    OKTA_DOMAIN_CREATE_CERTIFICATE = ("okta", "okta_domain_create_certificate", False)
    OKTA_DOMAIN_VERIFY_BY_ID = ("okta", "okta_domain_verify_by_id", False)
    OKTA_EVENT_HOOK_LIST_SUCCESS_EVENTS = (
        "okta",
        "okta_event_hook_list_success_events",
        False,
    )
    OKTA_EVENT_HOOK_CREATE_SUCCESS = ("okta", "okta_event_hook_create_success", False)
    OKTA_EVENT_HOOK_REMOVE_SUCCESS_EVENT = (
        "okta",
        "okta_event_hook_remove_success_event",
        False,
    )
    OKTA_EVENT_HOOK_GET_SUCCESS_EVENT = (
        "okta",
        "okta_event_hook_get_success_event",
        False,
    )
    OKTA_EVENT_HOOK_UPDATE_SUCCESS_EVENT = (
        "okta",
        "okta_event_hook_update_success_event",
        False,
    )
    OKTA_EVENT_HOOK_ACTIVATE_LIFECYCLE_SUCCESS = (
        "okta",
        "okta_event_hook_activate_lifecycle_success",
        False,
    )
    OKTA_EVENT_HOOK_DEACTIVATE_LIFECYCLE_EVENT = (
        "okta",
        "okta_event_hook_deactivate_lifecycle_event",
        False,
    )
    OKTA_EVENT_HOOK_VERIFY_LIFECYCLE_SUCCESS = (
        "okta",
        "okta_event_hook_verify_lifecycle_success",
        False,
    )
    OKTA_FEATURE_GET_SUCCESS = ("okta", "okta_feature_get_success", False)
    OKTA_FEATURE_GET_SUCCESS_BY_ID = ("okta", "okta_feature_get_success_by_id", False)
    OKTA_FEATURE_LIST_DEPENDENCIES = ("okta", "okta_feature_list_dependencies", False)
    OKTA_FEATURE_LIST_DEPENDENTS = ("okta", "okta_feature_list_dependents", False)
    OKTA_FEATURE_CREATE_LIFECYCLE_SUCCESS = (
        "okta",
        "okta_feature_create_lifecycle_success",
        False,
    )
    OKTA_GROUP_LIST = ("okta", "okta_group_list", False)
    OKTA_GROUP_CREATE_NEW_GROUP = ("okta", "okta_group_create_new_group", False)
    OKTA_GROUP_GET_ALL_RULES = ("okta", "okta_group_get_all_rules", False)
    OKTA_GROUP_ADD_RULE = ("okta", "okta_group_add_rule", False)
    OKTA_GROUP_REMOVE_RULE_BY_ID = ("okta", "okta_group_remove_rule_by_id", False)
    OKTA_GROUP_GET_GROUP_RULE_BY_ID = ("okta", "okta_group_get_group_rule_by_id", False)
    OKTA_GROUP_UPDATE_RULE = ("okta", "okta_group_update_rule", False)
    OKTA_GROUP_ACTIVATE_RULE_LIFECYCLE = (
        "okta",
        "okta_group_activate_rule_lifecycle",
        False,
    )
    OKTA_GROUP_DEACTIVATE_RULE_LIFECYCLE = (
        "okta",
        "okta_group_deactivate_rule_lifecycle",
        False,
    )
    OKTA_GROUP_REMOVE_OPERATION = ("okta", "okta_group_remove_operation", False)
    OKTA_GROUP_GET_RULES = ("okta", "okta_group_get_rules", False)
    OKTA_GROUP_UPDATE_PROFILE = ("okta", "okta_group_update_profile", False)
    OKTA_GROUP_LIST_ASSIGNED_APPS = ("okta", "okta_group_list_assigned_apps", False)
    OKTA_GROUP_GET_ROLE_LIST = ("okta", "okta_group_get_role_list", False)
    OKTA_GROUP_ASSIGN_ROLE_TO_GROUP = ("okta", "okta_group_assign_role_to_group", False)
    OKTA_GROUP_UN_ASSIGN_ROLE = ("okta", "okta_group_un_assign_role", False)
    OKTA_GROUP_GET_ROLE_SUCCESS = ("okta", "okta_group_get_role_success", False)
    OKTA_GROUP_GET_ROLE_TARGETS_CATALOG_APPS = (
        "okta",
        "okta_group_get_role_targets_catalog_apps",
        False,
    )
    OKTA_GROUP_DELETE_TARGET_GROUP_ROLES_CATALOG_APPS = (
        "okta",
        "okta_group_delete_target_group_roles_catalog_apps",
        False,
    )
    OKTA_GROUP_UPDATE_ROLES_CATALOG_APPS = (
        "okta",
        "okta_group_update_roles_catalog_apps",
        False,
    )
    OKTA_GROUP_REMOVE_APP_INSTANCE_TARGET_TO_APP_ADMIN_ROLE_GIVEN_TO_GROUP = (
        "okta",
        "okta_group_remove_app_instance_target_to_app_admin_role_given_to_group",
        False,
    )
    OKTA_GROUP_ADD_APP_INSTANCE_TARGET_TO_APP_ADMIN_ROLE_GIVEN_TO_GROUP = (
        "okta",
        "okta_group_add_app_instance_target_to_app_admin_role_given_to_group",
        False,
    )
    OKTA_GROUP_LIST_ROLE_TARGETS_GROUPS = (
        "okta",
        "okta_group_list_role_targets_groups",
        False,
    )
    OKTA_GROUP_REMOVE_TARGET_GROUP = ("okta", "okta_group_remove_target_group", False)
    OKTA_GROUP_UPDATE_TARGET_GROUPS_ROLE = (
        "okta",
        "okta_group_update_target_groups_role",
        False,
    )
    OKTA_GROUP_ENUMERATE_GROUP_MEMBERS = (
        "okta",
        "okta_group_enumerate_group_members",
        False,
    )
    OKTA_GROUP_REMOVE_USER_FROM = ("okta", "okta_group_remove_user_from", False)
    OKTA_GROUP_ADD_USER_TO_GROUP = ("okta", "okta_group_add_user_to_group", False)
    OKTA_IDENTITY_PROVIDER_LIST = ("okta", "okta_identity_provider_list", False)
    OKTA_IDENTITY_PROVIDER_ADD_NEW_IDP = (
        "okta",
        "okta_identity_provider_add_new_idp",
        False,
    )
    OKTA_IDENTITY_PROVIDER_ENUMERATE_IDP_KEYS = (
        "okta",
        "okta_identity_provider_enumerate_idp_keys",
        False,
    )
    OKTA_IDENTITY_PROVIDER_ADDX509_CERTIFICATE_PUBLIC_KEY = (
        "okta",
        "okta_identity_provider_addx509_certificate_public_key",
        False,
    )
    OKTA_IDENTITY_PROVIDER_DELETE_KEY_CREDENTIAL = (
        "okta",
        "okta_identity_provider_delete_key_credential",
        False,
    )
    OKTA_IDENTITY_PROVIDER_GET_KEY_CREDENTIAL_BY_IDP = (
        "okta",
        "okta_identity_provider_get_key_credential_by_idp",
        False,
    )
    OKTA_IDENTITY_PROVIDER_REMOVE_IDP = (
        "okta",
        "okta_identity_provider_remove_idp",
        False,
    )
    OKTA_IDENTITY_PROVIDER_GET_BY_IDP = (
        "okta",
        "okta_identity_provider_get_by_idp",
        False,
    )
    OKTA_IDENTITY_PROVIDER_UPDATE_CONFIGURATION = (
        "okta",
        "okta_identity_provider_update_configuration",
        False,
    )
    OKTA_IDENTITY_PROVIDER_LIST_CSRS_FOR_CERTIFICATE_SIGNING_REQUESTS = (
        "okta",
        "okta_identity_provider_list_csrs_for_certificate_signing_requests",
        False,
    )
    OKTA_IDENTITY_PROVIDER_GENERATE_CSR = (
        "okta",
        "okta_identity_provider_generate_csr",
        False,
    )
    OKTA_IDENTITY_PROVIDER_REVOKE_CSR_FOR_IDENTITY_PROVIDER = (
        "okta",
        "okta_identity_provider_revoke_csr_for_identity_provider",
        False,
    )
    OKTA_IDENTITY_PROVIDER_GET_CSR_BY_IDP = (
        "okta",
        "okta_identity_provider_get_csr_by_idp",
        False,
    )
    OKTA_IDENTITY_PROVIDER_UPDATE_CSR_LIFECYCLE_PUBLISH = (
        "okta",
        "okta_identity_provider_update_csr_lifecycle_publish",
        False,
    )
    OKTA_IDENTITY_PROVIDER_LIST_SIGNING_KEY_CREDENTIALS = (
        "okta",
        "okta_identity_provider_list_signing_key_credentials",
        False,
    )
    OKTA_IDENTITY_PROVIDER_GENERATE_NEW_SIGNING_KEY_CREDENTIAL = (
        "okta",
        "okta_identity_provider_generate_new_signing_key_credential",
        False,
    )
    OKTA_IDENTITY_PROVIDER_GET_SIGNING_KEY_CREDENTIAL_BY_IDP = (
        "okta",
        "okta_identity_provider_get_signing_key_credential_by_idp",
        False,
    )
    OKTA_IDENTITY_PROVIDER_CLONE_SIGNING_KEY_CREDENTIAL = (
        "okta",
        "okta_identity_provider_clone_signing_key_credential",
        False,
    )
    OKTA_IDENTITY_PROVIDER_ACTIVATE_IDP_LIFECYCLE = (
        "okta",
        "okta_identity_provider_activate_idp_lifecycle",
        False,
    )
    OKTA_IDENTITY_PROVIDER_DEACTIVATE_IDP = (
        "okta",
        "okta_identity_provider_deactivate_idp",
        False,
    )
    OKTA_IDENTITY_PROVIDER_GET_USER = ("okta", "okta_identity_provider_get_user", False)
    OKTA_IDENTITY_PROVIDE_RUN_LINK_USER = (
        "okta",
        "okta_identity_provide_run_link_user",
        False,
    )
    OKTA_IDENTITY_PROVIDER_GET_LINKED_USER_BY_ID = (
        "okta",
        "okta_identity_provider_get_linked_user_by_id",
        False,
    )
    OKTA_IDENTITY_PROVIDER_LINK_USER_TO_IDP_WITHOUT_TRANSACTION = (
        "okta",
        "okta_identity_provider_link_user_to_idp_without_transaction",
        False,
    )
    OKTA_IDENTITY_PROVIDER_GET_SOCIAL_AU_TH_TOKENS = (
        "okta",
        "okta_identity_provider_get_social_au_th_tokens",
        False,
    )
    OKTA_INLINE_HOOK_GET_SUCCESS = ("okta", "okta_inline_hook_get_success", False)
    OKTA_INLINE_HOOK_CREATE_SUCCESS = ("okta", "okta_inline_hook_create_success", False)
    OKTA_INLINE_HOOK_DELETE_MATCHING_BY_ID = (
        "okta",
        "okta_inline_hook_delete_matching_by_id",
        False,
    )
    OKTA_INLINE_HOOK_GET_BY_ID = ("okta", "okta_inline_hook_get_by_id", False)
    OKTA_INLINE_HOOK_UPDATE_BY_ID = ("okta", "okta_inline_hook_update_by_id", False)
    OKTA_INLINE_HOOK_ACTIVATE_LIFECYCLE = (
        "okta",
        "okta_inline_hook_activate_lifecycle",
        False,
    )
    OKTA_INLINE_HOOK_DEACTIVATE_LIFECYCLE = (
        "okta",
        "okta_inline_hook_deactivate_lifecycle",
        False,
    )
    OKTA_LOG_GET_LIST_EVENTS = ("okta", "okta_log_get_list_events", False)
    OKTA_PROFILE_MAPPING_LIST_WITH_PAGINATION = (
        "okta",
        "okta_profile_mapping_list_with_pagination",
        False,
    )
    OKTA_PROFILE_MAPPING_GET_BY_ID = ("okta", "okta_profile_mapping_get_by_id", False)
    OKTA_PROFILE_MAPPING_UPDATE_PROPERTY_MAPPINGS = (
        "okta",
        "okta_profile_mapping_update_property_mappings",
        False,
    )
    OKTA_USER_SCHEMA_GET_USER_SCHEMA = (
        "okta",
        "okta_user_schema_get_user_schema",
        False,
    )
    OKTA_GROUP_SCHEMA_GET = ("okta", "okta_group_schema_get", False)
    OKTA_LINKED_OBJECT_GET_USER_LINKED_OBJECTS = (
        "okta",
        "okta_linked_object_get_user_linked_objects",
        False,
    )
    OKTA_LINKED_OBJECT_CREATE_LINKED_OBJECT = (
        "okta",
        "okta_linked_object_create_linked_object",
        False,
    )
    OKTA_LINKED_OBJECT_DELETE_USER_LINKED_OBJECT = (
        "okta",
        "okta_linked_object_delete_user_linked_object",
        False,
    )
    OKTA_LINKED_OBJECT_GET_USER_LINKED_OBJECTS2 = (
        "okta",
        "okta_linked_object_get_user_linked_objects2",
        False,
    )
    OKTA_USER_SCHEMA_GET_SCHEMA_BY_ID = (
        "okta",
        "okta_user_schema_get_schema_by_id",
        False,
    )
    OKTA_USER_TYPE_GET_ALL_USER_TYPES = (
        "okta",
        "okta_user_type_get_all_user_types",
        False,
    )
    OKTA_USER_TYPE_CREATE_NEW_USER_TYPE = (
        "okta",
        "okta_user_type_create_new_user_type",
        False,
    )
    OKTA_USER_TYPE_DELETE_PERMANENTLY = (
        "okta",
        "okta_user_type_delete_permanently",
        False,
    )
    OKTA_USER_TYPE_GET_BY_ID = ("okta", "okta_user_type_get_by_id", False)
    OKTA_USER_TYPE_UPDATE_EXISTING_TYPE = (
        "okta",
        "okta_user_type_update_existing_type",
        False,
    )
    OKTA_USER_TYPEREPLACE_EXISTING_TYPE = (
        "okta",
        "okta_user_typereplace_existing_type",
        False,
    )
    OKTA_ORG_GET_SETTINGS = ("okta", "okta_org_get_settings", False)
    OKTA_ORG_UPDATE_SETTINGS = ("okta", "okta_org_update_settings", False)
    OKTA_ORG_UPDATE_SETTING = ("okta", "okta_org_update_setting", False)
    OKTA_ORG_LIST_CONTACT_TYPES = ("okta", "okta_org_list_contact_types", False)
    OKTA_ORG_GET_CONTACT_USER = ("okta", "okta_org_get_contact_user", False)
    OKTA_ORG_UPDATE_CONTACT_USER = ("okta", "okta_org_update_contact_user", False)
    OKTA_ORG_UPDATE_ORGANIZATION_LOGO = (
        "okta",
        "okta_org_update_organization_logo",
        False,
    )
    OKTA_ORG_GET_ORG_PREFERENCES = ("okta", "okta_org_get_org_preferences", False)
    OKTA_ORG_HIDE_END_USER_FOOTER = ("okta", "okta_org_hide_end_user_footer", False)
    OKTA_ORG_MAKE_OK_TAUI_FOOTER_VISIBLE = (
        "okta",
        "okta_org_make_ok_taui_footer_visible",
        False,
    )
    OKTA_ORG_GETO_KTA_COMMUNICATION_SETTINGS = (
        "okta",
        "okta_org_geto_kta_communication_settings",
        False,
    )
    OKTA_OR_GO_PTI_NO_KTA_COMMUNICATION_EMAILS = (
        "okta",
        "okta_or_go_pti_no_kta_communication_emails",
        False,
    )
    OKTA_OR_GOP_TOU_TO_KTA_COMMUNICATION_EMAILS = (
        "okta",
        "okta_or_gop_tou_to_kta_communication_emails",
        False,
    )
    OKTA_ORG_GETO_KTA_SUPPORT_SETTINGS = (
        "okta",
        "okta_org_geto_kta_support_settings",
        False,
    )
    OKTA_ORG_EXTENDO_KTA_SUPPORT = ("okta", "okta_org_extendo_kta_support", False)
    OKTA_ORG_GRAN_TO_KTA_SUPPORT_ACCESS = (
        "okta",
        "okta_org_gran_to_kta_support_access",
        False,
    )
    OKTA_ORG_EXTENDO_KTA_SUPPORT2 = ("okta", "okta_org_extendo_kta_support2", False)
    OKTA_POLICY_GET_ALL_WITH_TYPE = ("okta", "okta_policy_get_all_with_type", False)
    OKTA_POLICY_CREATE_NEW_POLICY = ("okta", "okta_policy_create_new_policy", False)
    OKTA_POLICY_REMOVE_POLICY_OPERATION = (
        "okta",
        "okta_policy_remove_policy_operation",
        False,
    )
    OKTA_POLICY_GET_POLICY = ("okta", "okta_policy_get_policy", False)
    OKTA_POLICY_UPDATE_OPERATION = ("okta", "okta_policy_update_operation", False)
    OKTA_POLICY_ACTIVATE_LIFECYCLE = ("okta", "okta_policy_activate_lifecycle", False)
    OKTA_POLICY_DEACTIVATE_LIFECYCLE = (
        "okta",
        "okta_policy_deactivate_lifecycle",
        False,
    )
    OKTA_POLICY_ENUMERATE_RULES = ("okta", "okta_policy_enumerate_rules", False)
    OKTA_POLICY_CREATE_RULE = ("okta", "okta_policy_create_rule", False)
    OKTA_POLICY_REMOVE_RULE = ("okta", "okta_policy_remove_rule", False)
    OKTA_POLICY_GET_POLICY_RULE = ("okta", "okta_policy_get_policy_rule", False)
    OKTA_POLICY_UPDATE_RULE = ("okta", "okta_policy_update_rule", False)
    OKTA_POLICY_ACTIVATE_RULE_LIFECYCLE = (
        "okta",
        "okta_policy_activate_rule_lifecycle",
        False,
    )
    OKTA_POLICY_DEACTIVATE_RULE_LIFECYCLE = (
        "okta",
        "okta_policy_deactivate_rule_lifecycle",
        False,
    )
    OKTA_SUBSCRIPTION_LIST_ROLE_SUBSCRIPTIONS = (
        "okta",
        "okta_subscription_list_role_subscriptions",
        False,
    )
    OKTA_SUBSCRIPTION_GET_ROLE_SUBSCRIPTIONS_BY_NOTIFICATION_TYPE = (
        "okta",
        "okta_subscription_get_role_subscriptions_by_notification_type",
        False,
    )
    OKTA_SUBSCRIPTION_ROLE_NOTIFICATION_SUBSCRIBE = (
        "okta",
        "okta_subscription_role_notification_subscribe",
        False,
    )
    OKTA_SUBSCRIPTION_CUSTOM_ROLE_NOTIFICATION_UNSUBSCRIBE = (
        "okta",
        "okta_subscription_custom_role_notification_unsubscribe",
        False,
    )
    OKTA_SESSION_CREATE_SESSION_WITH_TOKEN = (
        "okta",
        "okta_session_create_session_with_token",
        False,
    )
    OKTA_SESSION_CLOSE = ("okta", "okta_session_close", False)
    OKTA_SESSION_GET_DETAILS = ("okta", "okta_session_get_details", False)
    OKTA_SESSION_REFRESH_LIFECYCLE = ("okta", "okta_session_refresh_lifecycle", False)
    OKTA_TEMPLATE_ENUMERATES_MS_TEMPLATES = (
        "okta",
        "okta_template_enumerates_ms_templates",
        False,
    )
    OKTA_TEMPLATE_ADD_NEW_CUSTOMS_MS = (
        "okta",
        "okta_template_add_new_customs_ms",
        False,
    )
    OKTA_TEMPLATE_REMOVES_MS = ("okta", "okta_template_removes_ms", False)
    OKTA_TEMPLATE_GET_BY_ID = ("okta", "okta_template_get_by_id", False)
    OKTA_TEMPLATE_PARTIAL_SMS_UPDATE = (
        "okta",
        "okta_template_partial_sms_update",
        False,
    )
    OKTA_TEMPLATE_UPDATES_MS_TEMPLATE = (
        "okta",
        "okta_template_updates_ms_template",
        False,
    )
    OKTA_THREAT_INSIGHT_GET_CURRENT_CONFIGURATION = (
        "okta",
        "okta_threat_insight_get_current_configuration",
        False,
    )
    OKTA_THREAT_INSIGHT_UPDATE_CONFIGURATION = (
        "okta",
        "okta_threat_insight_update_configuration",
        False,
    )
    OKTA_TRUSTED_ORIGIN_GET_LIST = ("okta", "okta_trusted_origin_get_list", False)
    OKTA_TRUSTED_ORIGIN_CREATE_SUCCESS = (
        "okta",
        "okta_trusted_origin_create_success",
        False,
    )
    OKTA_TRUSTED_ORIGIN_DELETE_SUCCESS = (
        "okta",
        "okta_trusted_origin_delete_success",
        False,
    )
    OKTA_TRUSTED_ORIGIN_GET_SUCCESS_BY_ID = (
        "okta",
        "okta_trusted_origin_get_success_by_id",
        False,
    )
    OKTA_TRUSTED_ORIGIN_UPDATE_SUCCESS = (
        "okta",
        "okta_trusted_origin_update_success",
        False,
    )
    OKTA_TRUSTED_ORIGIN_ACTIVATE_LIFECYCLE_SUCCESS = (
        "okta",
        "okta_trusted_origin_activate_lifecycle_success",
        False,
    )
    OKTA_TRUSTED_ORIGIN_DEACTIVATE_LIFECYCLE_SUCCESS = (
        "okta",
        "okta_trusted_origin_deactivate_lifecycle_success",
        False,
    )
    OKTA_USER_LIST_ACTIVE_USERS = ("okta", "okta_user_list_active_users", False)
    OKTA_USER_CREATE_NEW_USER = ("okta", "okta_user_create_new_user", False)
    OKTA_USER_UPDATE_LINKED_OBJECT = ("okta", "okta_user_update_linked_object", False)
    OKTA_USER_DELETE_PERMANENTLY = ("okta", "okta_user_delete_permanently", False)
    OKTA_USER_GETO_KTA_USER = ("okta", "okta_user_geto_kta_user", False)
    OKTA_USER_UPDATE_PROFILE = ("okta", "okta_user_update_profile", False)
    OKTA_USER_UPDATE_PROFILE2 = ("okta", "okta_user_update_profile2", False)
    OKTA_USER_LIST_ASSIGNED_APP_LINKS = (
        "okta",
        "okta_user_list_assigned_app_links",
        False,
    )
    OKTA_USER_LIST_CLIENTS = ("okta", "okta_user_list_clients", False)
    OKTA_USER_REVOKE_GRANTS_FOR_USER_AND_CLIENT = (
        "okta",
        "okta_user_revoke_grants_for_user_and_client",
        False,
    )
    OKTA_USER_LIST_GRANTS_FOR_CLIENT = (
        "okta",
        "okta_user_list_grants_for_client",
        False,
    )
    OKTA_USER_REVOKE_ALL_TOKENS = ("okta", "okta_user_revoke_all_tokens", False)
    OKTA_USER_LIST_REFRESH_TOKENS_FOR_USER_AND_CLIENT = (
        "okta",
        "okta_user_list_refresh_tokens_for_user_and_client",
        False,
    )
    OKTA_USER_REVOKE_TOKEN_FOR_CLIENT = (
        "okta",
        "okta_user_revoke_token_for_client",
        False,
    )
    OKTA_USER_GET_CLIENT_REFRESH_TOKEN = (
        "okta",
        "okta_user_get_client_refresh_token",
        False,
    )
    OKTA_USER_CHANGE_PASSWORD_VALIDATION = (
        "okta",
        "okta_user_change_password_validation",
        False,
    )
    OKTA_USER_UPDATE_RECOVERY_QUESTION = (
        "okta",
        "okta_user_update_recovery_question",
        False,
    )
    OKTA_USER_FORGOT_PASSWORD = ("okta", "okta_user_forgot_password", False)
    OKTA_USER_FACTOR_ENUMERATE_ENROLLED = (
        "okta",
        "okta_user_factor_enumerate_enrolled",
        False,
    )
    OKTA_USER_FACTOR_ENROLL_SUPPORTED_FACTOR = (
        "okta",
        "okta_user_factor_enroll_supported_factor",
        False,
    )
    OKTA_USER_FACTOR_ENUMERATE_SUPPORTED_FACTORS = (
        "okta",
        "okta_user_factor_enumerate_supported_factors",
        False,
    )
    OKTA_USER_FACTOR_ENUMERATE_SECURITY_QUESTIONS = (
        "okta",
        "okta_user_factor_enumerate_security_questions",
        False,
    )
    OKTA_USER_FACTO_RUN_ENROLL_FACTOR = (
        "okta",
        "okta_user_facto_run_enroll_factor",
        False,
    )
    OKTA_USER_FACTOR_GET_FACTOR = ("okta", "okta_user_factor_get_factor", False)
    OKTA_USER_FACTOR_ACTIVATE_FACTOR_LIFECYCLE = (
        "okta",
        "okta_user_factor_activate_factor_lifecycle",
        False,
    )
    OKTA_USER_FACTOR_POLL_FACTOR_TRANSACTION_STATUS = (
        "okta",
        "okta_user_factor_poll_factor_transaction_status",
        False,
    )
    OKTA_USER_FACTOR_VERIFY_OTP = ("okta", "okta_user_factor_verify_otp", False)
    OKTA_USER_REVOKE_GRANTS = ("okta", "okta_user_revoke_grants", False)
    OKTA_USER_LIST_GRANTS = ("okta", "okta_user_list_grants", False)
    OKTA_USER_REVOKE_GRANT = ("okta", "okta_user_revoke_grant", False)
    OKTA_USER_GET_GRANT_BY_ID = ("okta", "okta_user_get_grant_by_id", False)
    OKTA_USER_GET_MEMBER_GROUPS = ("okta", "okta_user_get_member_groups", False)
    OKTA_USER_LISTI_DPS_FOR_USER = ("okta", "okta_user_listi_dps_for_user", False)
    OKTA_USER_ACTIVATE_LIFECYCLE = ("okta", "okta_user_activate_lifecycle", False)
    OKTA_USER_DEACTIVATE_LIFECYCLE = ("okta", "okta_user_deactivate_lifecycle", False)
    OKTA_USER_EXPIRE_PASSWORD_AND_GET_TEMPORARY_PASSWORD = (
        "okta",
        "okta_user_expire_password_and_get_temporary_password",
        False,
    )
    OKTA_USER_EXPIRE_PASSWORD_AND_TEMPORARY_PASSWORD = (
        "okta",
        "okta_user_expire_password_and_temporary_password",
        False,
    )
    OKTA_USER_REACTIVATE_USER = ("okta", "okta_user_reactivate_user", False)
    OKTA_USER_RESET_FACTORS_OPERATION = (
        "okta",
        "okta_user_reset_factors_operation",
        False,
    )
    OKTA_USER_GENERATE_PASSWORD_RESET_TOKEN = (
        "okta",
        "okta_user_generate_password_reset_token",
        False,
    )
    OKTA_USER_SUSPEND_LIFECYCLE = ("okta", "okta_user_suspend_lifecycle", False)
    OKTA_USER_UNLOCK_USER_STATUS = ("okta", "okta_user_unlock_user_status", False)
    OKTA_USE_RUN_SUSPEND_LIFECYCLE = ("okta", "okta_use_run_suspend_lifecycle", False)
    OKTA_USER_DELETE_LINKED_OBJECTS = ("okta", "okta_user_delete_linked_objects", False)
    OKTA_USER_GET_LINKED_OBJECTS = ("okta", "okta_user_get_linked_objects", False)
    OKTA_USER_LIST_ASSIGNED_ROLES = ("okta", "okta_user_list_assigned_roles", False)
    OKTA_USER_ASSIGN_ROLE = ("okta", "okta_user_assign_role", False)
    OKTA_USE_RUN_ASSIGN_ROLE = ("okta", "okta_use_run_assign_role", False)
    OKTA_USER_GET_ASSIGNED_ROLE = ("okta", "okta_user_get_assigned_role", False)
    OKTA_USER_LIST_APP_TARGETS_FOR_ROLE = (
        "okta",
        "okta_user_list_app_targets_for_role",
        False,
    )
    OKTA_USER_UPDATE_ROLES_CATALOG_APPS = (
        "okta",
        "okta_user_update_roles_catalog_apps",
        False,
    )
    OKTA_USER_DELETE_TARGET_APP = ("okta", "okta_user_delete_target_app", False)
    OKTA_USER_UPDATE_ROLES_CATALOG_APPS2 = (
        "okta",
        "okta_user_update_roles_catalog_apps2",
        False,
    )
    OKTA_USER_REMOVE_APP_INSTANCE_TARGET_TO_APP_ADMINISTRATOR_ROLE_GIVEN_TO = (
        "okta",
        "okta_user_remove_app_instance_target_to_app_administrator_role_given_to",
        False,
    )
    OKTA_USER_ADD_APP_INSTANCE_TARGET_TO_APP_ADMINISTRATOR_ROLE_GIVEN_TO_USER = (
        "okta",
        "okta_user_add_app_instance_target_to_app_administrator_role_given_to_user",
        False,
    )
    OKTA_USER_LIST_ROLE_TARGETS_GROUPS = (
        "okta",
        "okta_user_list_role_targets_groups",
        False,
    )
    OKTA_USER_REMOVE_TARGET_GROUP = ("okta", "okta_user_remove_target_group", False)
    OKTA_USER_UPDATE_ROLES_CATALOG_APPS3 = (
        "okta",
        "okta_user_update_roles_catalog_apps3",
        False,
    )
    OKTA_USER_REVOKE_ALL_SESSIONS = ("okta", "okta_user_revoke_all_sessions", False)
    OKTA_USER_LIST_SUBSCRIPTIONS = ("okta", "okta_user_list_subscriptions", False)
    OKTA_USER_GET_SUBSCRIPTION_BY_NOTIFICATION = (
        "okta",
        "okta_user_get_subscription_by_notification",
        False,
    )
    OKTA_SUBSCRIPTION_USER_NOTIFICATION_SUBSCRIBE = (
        "okta",
        "okta_subscription_user_notification_subscribe",
        False,
    )
    OKTA_SUBSCRIPTION_UNSUBSCRIBE_USER_SUBSCRIPTION_BY_NOTIFICATION_TYPE = (
        "okta",
        "okta_subscription_unsubscribe_user_subscription_by_notification_type",
        False,
    )
    OKTA_NETWORK_ZONE_LIST_ZONES = ("okta", "okta_network_zone_list_zones", False)
    OKTA_NETWORK_ZONE_CREATE_NEW = ("okta", "okta_network_zone_create_new", False)
    OKTA_NETWORK_ZONE_REMOVE_ZONE = ("okta", "okta_network_zone_remove_zone", False)
    OKTA_NETWORK_ZONE_GET_BY_ID = ("okta", "okta_network_zone_get_by_id", False)
    OKTA_NETWORK_ZONE_UPDATE_ZONE = ("okta", "okta_network_zone_update_zone", False)
    OKTA_NETWORK_ZONE_ACTIVATE_LIFECYCLE = (
        "okta",
        "okta_network_zone_activate_lifecycle",
        False,
    )
    OKTA_NETWORK_ZONE_DEACTIVATE_ZONE_LIFECYCLE = (
        "okta",
        "okta_network_zone_deactivate_zone_lifecycle",
        False,
    )
    TEST_ASANA_CREATE_SUBTASK = ("test_asana", "test_asana_create_subtask", False)
    TEST_ASANA_GET_SUBTASKS = ("test_asana", "test_asana_get_subtasks", False)


class Trigger(Enum):
    def __init__(self, service, trigger):
        self.service = service
        self.trigger = trigger

    GITHUB_PULL_REQUEST_EVENT = ("github", "github_pull_request_event")
    GITHUB_COMMIT_EVENT = ("github", "github_commit_event")
    SLACK_NEW_MESSAGE = ("slack", "slack_receive_message")
    SLACKBOT_NEW_MESSAGE = ("slackbot", "slackbot_receive_message")
