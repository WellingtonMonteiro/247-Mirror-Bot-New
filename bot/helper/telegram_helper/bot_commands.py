import os

def getCommand(name: str, command: str):
    try:
        if len(os.environ[name]) == 0:
            raise KeyError
        return os.environ[name]
    except KeyError:
        return command

class _BotCommands:
    def __init__(self):
        self.StartCommand = getCommand('START_BOT', 'start')
        self.MirrorCommand = getCommand('MIRROR_BOT', 'mirror3')
        self.UnzipMirrorCommand = getCommand('UNZIPMIR_BOT', 'unzipmirror3')
        self.TarMirrorCommand = getCommand('TARMIR_BOT', 'tarmirror3')
        self.ZipMirrorCommand = getCommand('ZIPMIR_BOT', 'zipmirror3')
        self.CancelMirror = getCommand('CANCEL_BOT', 'cancel')
        self.CancelAllCommand = getCommand('CANCEL_ALL_BOT', 'cancelall')
        self.ListCommand = getCommand('LIST_BOT', 'list')
        self.StatusCommand = getCommand('STATUS_BOT', 'status')
        self.AuthorizedUsersCommand = getCommand('USERS_BOT', 'users')
        self.AuthorizeCommand = getCommand('AUTH_BOT', 'auth')
        self.UnAuthorizeCommand = getCommand('UNAUTH_BOT', 'unauth')
        self.AddSudoCommand = getCommand('ADDSUDO_BOT', 'addsudo')
        self.RmSudoCommand = getCommand('RMSUDO_BOT', 'rmsudo')
        self.PingCommand = getCommand('PING_BOT', 'ping')
        self.RestartCommand = getCommand('RESTART_BOT', 'restart')
        self.StatsCommand = getCommand('STATS_BOT', 'stats')
        self.HelpCommand = getCommand('HELP_BOT', 'help')
        self.LogCommand = getCommand('LOG_BOT', 'log')
        self.SpeedCommand = getCommand('SPEED_BOT', 'speedtest')
        self.CloneCommand = getCommand('CLONE_BOT', 'cloneg')
        self.CountCommand = getCommand('COUNT_BOT', 'countg')
        self.WatchCommand = getCommand('WATCH_BOT', 'watch3')
        self.TarWatchCommand = getCommand('TARWATCH_BOT', 'tarwatch3')
        self.ZipWatchCommand = getCommand('ZIPWATCH_BOT', 'zipwatch3')
        self.QbMirrorCommand = getCommand('QBMIRROR_BOT', 'qbmirror3')
        self.QbUnzipMirrorCommand = getCommand('QBUNZIPMIRROR_BOT', 'qbunzipmirror3')
        self.QbTarMirrorCommand = getCommand('QBTARMIRROR_BOT', 'qbtarmirror3')
        self.QbZipMirrorCommand = getCommand('QBZIPMIRROR_BOT', 'qbzipmirror3')
        self.DeleteCommand = getCommand('DEL_BOT', 'del')
        self.ShellCommand = getCommand('SHELL_BOT', 'shell')
        self.ExecHelpCommand = getCommand('EXECHELP_BOT', 'exchelp')
        self.TsHelpCommand = getCommand('TSHELP_BOT', 'tshelp')
        self.LeechSetCommand = getCommand('LEECHSET_BOT', 'leechset')
        self.SetThumbCommand = getCommand('SETTHUMB_BOT', 'setthumb3')
        self.LeechCommand = getCommand('LEECH_BOT', 'leech3')
        self.TarLeechCommand = getCommand('TARLEECH_BOT', 'tarleech3')
        self.UnzipLeechCommand = getCommand('UNZIPLEECH_BOT', 'unzipleech3')
        self.ZipLeechCommand = getCommand('ZIPLEECH_BOT', 'zipleech3')
        self.QbLeechCommand = getCommand('QBLEECH_BOT', 'qbleech3')
        self.QbTarLeechCommand = getCommand('QBTARLEECH_BOT', 'qbtarleech3')
        self.QbUnzipLeechCommand = getCommand('QBUNZIPLEECH_BOT', 'qbunzipleech3')
        self.QbZipLeechCommand = getCommand('QBZIPLEECH_BOT', 'qbzipleech3')
        self.LeechWatchCommand = getCommand('LEECHWATCH_BOT', 'leechwatch3')
        self.LeechTarWatchCommand = getCommand('LEECHTARWATCH_BOT', 'leechtarwatch3')
        self.LeechZipWatchCommand = getCommand('LEECHZIPWATCH_BOT', 'leechzipwatch3')

BotCommands = _BotCommands()
