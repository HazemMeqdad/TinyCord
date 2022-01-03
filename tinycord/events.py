class Events:
    """
        A class that connect the events to our name events.
    """
    messageCreate = 'on_message'
    messageUpdate = 'on_message_update'
    messageDelete = 'on_message_delete'
    messageReactionAdd = 'on_message_reaction_add'
    messageReactionRemove = 'on_message_reaction_remove'

    guildJoin = 'on_guild_join'
    guildUpdate = 'on_guild_update'
    guildDelete = 'on_guild_delete'
    guildCache = 'on_guild_cache'

    guildBanAdd = 'on_guild_ban_add'
    guildBanRemove = 'on_guild_ban_remove'

    inviteCreate = 'on_invite_create'
    inviteDelete = 'on_invite_delete'

    integrationCreate = 'on_integration_create'
    integrationUpdate = 'on_integration_update'
    integrationDelete = 'on_integration_delete'

    scheduledCreate = 'on_scheduled_create'
    scheduledDelete = 'on_scheduled_delete'
    scheduledUpdate = 'on_scheduled_update'
    scheduledUserAdd = 'on_scheduled_user_add'
    scheduledUserRemove = 'on_scheduled_user_remove'

    roleCreate = 'on_role_create'
    roleUpdate = 'on_role_update'
    roleDelete = 'on_role_delete'

    memberJoin = 'on_member_join'
    memberUpdate = 'on_member_update'
    memberDelete = 'on_member_delete'

    channelCreate = 'on_channel_create'
    channelUpdate = 'on_channel_update'
    channelDelete = 'on_channel_delete'

    threadCreate = 'on_thread_create'
    threadUpdate = 'on_thread_update'
    threadDelete = 'on_thread_delete'
    
    stageInstanceCreate = 'on_stage_instance_create'
    stageInstanceUpdate = 'on_stage_instance_update'
    stageInstanceDelete = 'on_stage_instance_delete'

    userUpdate = 'on_user_update'

    voiceStateUpdate = 'on_voice_state_update'

    ready = 'on_ready'
    shardReady = 'on_ready'