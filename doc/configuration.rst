Configuration
=============

Bot configuration
-----------------

The bot configuration is made on tontonbot/setting.py file.

Example:

.. code-block:: python

    VERSION = "v0.2b"                                   # The bot version
    quitMessage = "Good bye."                           # Message that will be displayed on quit
    owner = "tonton"                                    # owner nickname, the owner can reload plugins or quit
    server = "irc.evolu.net"                            # irc server
    port = 6667                                         # irc port
    channel = "#legarageabot"                           # channel
    nickname = "tonton-bot"                             # The bot nickname
    logFile = "./tonton-bot.log"                        # Path to the log file
    pluginConfigFile = "tontonbot/plugins/settings.xml" # plugin config

Plugin configuration
--------------------

Configuration is made on a xml file.
The path to this file is set on setting.py

Each plugin needs a configuration to run.

Example:

.. code-block:: xml

    <plugin>
        <name>HelloToto</name>             <!-- The plugin name (mandatory) -->
        <file>say.Say</file>               <!-- The plugin filename (mandatory) -->
        <command>!hi</command>             <!-- command triggering the plugin (only if it is a command plugin) -->
        <config>                           <!-- The configuration for the plugin (depending on the plugin) -->
            <message>Hello.</message>
        </config>
        <events>                           <!-- irc event list triggering this plugin (mandatory) -->
            <event>JOIN</event>
        </events>
        <security>
            <whitelist>                    <!-- user list allowed for this command (all users if blank) -->
                <user>toto</user>
            </whitelist>
            <blacklist>                    <!-- user list not allowed for this command (all users if blank) -->
                <user>tonton</user>
            </blacklist>
        </security>
        <description>                      <!-- plugin description (mandatory) -->
            Displays a message when the toto user joins.
        </description>
    </plugin>
