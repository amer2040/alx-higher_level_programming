{"payload":{"allShortcutsEnabled":false,"fileTree":{"0x15-javascript-web_jquery":{"items":[{"name":"0-main.html","path":"0x15-javascript-web_jquery/0-main.html","contentType":"file"},{"name":"0-script.js","path":"0x15-javascript-web_jquery/0-script.js","contentType":"file"},{"name":"1-script.js","path":"0x15-javascript-web_jquery/1-script.js","contentType":"file"},{"name":"100-script.js","path":"0x15-javascript-web_jquery/100-script.js","contentType":"file"},{"name":"101-script.js","path":"0x15-javascript-web_jquery/101-script.js","contentType":"file"},{"name":"102-script.js","path":"0x15-javascript-web_jquery/102-script.js","contentType":"file"},{"name":"103-script.js","path":"0x15-javascript-web_jquery/103-script.js","contentType":"file"},{"name":"2-script.js","path":"0x15-javascript-web_jquery/2-script.js","contentType":"file"},{"name":"3-script.js","path":"0x15-javascript-web_jquery/3-script.js","contentType":"file"},{"name":"4-script.js","path":"0x15-javascript-web_jquery/4-script.js","contentType":"file"},{"name":"5-script.js","path":"0x15-javascript-web_jquery/5-script.js","contentType":"file"},{"name":"6-script.js","path":"0x15-javascript-web_jquery/6-script.js","contentType":"file"},{"name":"7-script.js","path":"0x15-javascript-web_jquery/7-script.js","contentType":"file"},{"name":"8-script.js","path":"0x15-javascript-web_jquery/8-script.js","contentType":"file"},{"name":"9-script.js","path":"0x15-javascript-web_jquery/9-script.js","contentType":"file"},{"name":"README.md","path":"0x15-javascript-web_jquery/README.md","contentType":"file"},{"name":"push_all","path":"0x15-javascript-web_jquery/push_all","contentType":"file"}],"totalCount":17},"":{"items":[{"name":"0x00-python-hello_world","path":"0x00-python-hello_world","contentType":"directory"},{"name":"0x01-python-if_else_loops_functions","path":"0x01-python-if_else_loops_functions","contentType":"directory"},{"name":"0x02-python-import_modules","path":"0x02-python-import_modules","contentType":"directory"},{"name":"0x03-python-data_structures","path":"0x03-python-data_structures","contentType":"directory"},{"name":"0x04-python-more_data_structures","path":"0x04-python-more_data_structures","contentType":"directory"},{"name":"0x05-python-exceptions","path":"0x05-python-exceptions","contentType":"directory"},{"name":"0x06-python-classes","path":"0x06-python-classes","contentType":"directory"},{"name":"0x07-python-test_driven_development","path":"0x07-python-test_driven_development","contentType":"directory"},{"name":"0x08-python-more_classes","path":"0x08-python-more_classes","contentType":"directory"},{"name":"0x09-python-everything_is_object","path":"0x09-python-everything_is_object","contentType":"directory"},{"name":"0x0A-python-inheritance","path":"0x0A-python-inheritance","contentType":"directory"},{"name":"0x0B-python-input_output","path":"0x0B-python-input_output","contentType":"directory"},{"name":"0x0C-python-almost_a_circle","path":"0x0C-python-almost_a_circle","contentType":"directory"},{"name":"0x0D-SQL_introduction","path":"0x0D-SQL_introduction","contentType":"directory"},{"name":"0x0E-SQL_more_queries","path":"0x0E-SQL_more_queries","contentType":"directory"},{"name":"0x0F-python-object_relational_mapping","path":"0x0F-python-object_relational_mapping","contentType":"directory"},{"name":"0x10-python-network_0","path":"0x10-python-network_0","contentType":"directory"},{"name":"0x11-python-network_1","path":"0x11-python-network_1","contentType":"directory"},{"name":"0x12-javascript-warm_up","path":"0x12-javascript-warm_up","contentType":"directory"},{"name":"0x13-javascript_objects_scopes_closures","path":"0x13-javascript_objects_scopes_closures","contentType":"directory"},{"name":"0x14-javascript-web_scraping","path":"0x14-javascript-web_scraping","contentType":"directory"},{"name":"0x15-javascript-web_jquery","path":"0x15-javascript-web_jquery","contentType":"directory"},{"name":"test","path":"test","contentType":"file"}],"totalCount":23}},"fileTreeProcessingTime":5.215065,"foldersToFetch":[],"repo":{"id":649877417,"defaultBranch":"master","name":"alx-higher_level_programming","ownerLogin":"Ichrafsassi","currentUserCanPush":false,"isFork":false,"isEmpty":false,"createdAt":"2023-06-05T20:50:31.000Z","ownerAvatar":"https://avatars.githubusercontent.com/u/50300666?v=4","public":true,"private":false,"isOrgOwned":false},"symbolsExpanded":false,"treeExpanded":true,"refInfo":{"name":"master","listCacheKey":"v0:1685998826.592876","canEdit":false,"refType":"branch","currentOid":"c133ab13412841f3de2c09b5574758e10510724f"},"path":"0x15-javascript-web_jquery/8-script.js","currentUser":null,"blob":{"rawLines":["$.get('https://swapi.co/api/films/?format=json', function (data) {\r","  $('UL#list_movies').append(...data.results.map(movie => `<li>${movie.title}</li>`));\r","});\r"],"stylingDirectives":[[{"start":0,"end":1,"cssClass":"pl-s1"},{"start":1,"end":2,"cssClass":"pl-kos"},{"start":2,"end":5,"cssClass":"pl-en"},{"start":5,"end":6,"cssClass":"pl-kos"},{"start":6,"end":47,"cssClass":"pl-s"},{"start":47,"end":48,"cssClass":"pl-kos"},{"start":49,"end":57,"cssClass":"pl-k"},{"start":58,"end":59,"cssClass":"pl-kos"},{"start":59,"end":63,"cssClass":"pl-s1"},{"start":63,"end":64,"cssClass":"pl-kos"},{"start":65,"end":66,"cssClass":"pl-kos"}],[{"start":2,"end":3,"cssClass":"pl-en"},{"start":3,"end":4,"cssClass":"pl-kos"},{"start":4,"end":20,"cssClass":"pl-s"},{"start":20,"end":21,"cssClass":"pl-kos"},{"start":21,"end":22,"cssClass":"pl-kos"},{"start":22,"end":28,"cssClass":"pl-en"},{"start":28,"end":29,"cssClass":"pl-kos"},{"start":32,"end":36,"cssClass":"pl-s1"},{"start":36,"end":37,"cssClass":"pl-kos"},{"start":37,"end":44,"cssClass":"pl-c1"},{"start":44,"end":45,"cssClass":"pl-kos"},{"start":45,"end":48,"cssClass":"pl-en"},{"start":48,"end":49,"cssClass":"pl-kos"},{"start":49,"end":54,"cssClass":"pl-s1"},{"start":55,"end":57,"cssClass":"pl-c1"},{"start":58,"end":83,"cssClass":"pl-s"},{"start":63,"end":77,"cssClass":"pl-s1"},{"start":63,"end":65,"cssClass":"pl-kos"},{"start":65,"end":70,"cssClass":"pl-s1"},{"start":70,"end":71,"cssClass":"pl-kos"},{"start":71,"end":76,"cssClass":"pl-c1"},{"start":76,"end":77,"cssClass":"pl-kos"},{"start":83,"end":84,"cssClass":"pl-kos"},{"start":84,"end":85,"cssClass":"pl-kos"},{"start":85,"end":86,"cssClass":"pl-kos"}],[{"start":0,"end":1,"cssClass":"pl-kos"},{"start":1,"end":2,"cssClass":"pl-kos"},{"start":2,"end":3,"cssClass":"pl-kos"}]],"csv":null,"csvError":null,"dependabotInfo":{"showConfigurationBanner":false,"configFilePath":null,"networkDependabotPath":"/Ichrafsassi/alx-higher_level_programming/network/updates","dismissConfigurationNoticePath":"/settings/dismiss-notice/dependabot_configuration_notice","configurationNoticeDismissed":null},"displayName":"8-script.js","displayUrl":"https://github.com/Ichrafsassi/alx-higher_level_programming/blob/master/0x15-javascript-web_jquery/8-script.js?raw=true","headerInfo":{"blobSize":"161 Bytes","deleteTooltip":"You must be signed in to make or propose changes","editTooltip":"You must be signed in to make or propose changes","deleteInfo":{"deleteTooltip":"You must be signed in to make or propose changes"},"editInfo":{"editTooltip":"You must be signed in to make or propose changes"},"ghDesktopPath":"https://desktop.github.com","isGitLfs":false,"gitLfsPath":null,"onBranch":true,"shortPath":"861e232","siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2FIchrafsassi%2Falx-higher_level_programming%2Fblob%2Fmaster%2F0x15-javascript-web_jquery%2F8-script.js","isCSV":false,"isRichtext":false,"toc":null,"lineInfo":{"truncatedLoc":"3","truncatedSloc":"3"},"mode":"file"},"image":false,"isCodeownersFile":null,"isPlain":false,"isValidLegacyIssueTemplate":false,"issueTemplateHelpUrl":"https://docs.github.com/articles/about-issue-and-pull-request-templates","issueTemplate":null,"discussionTemplate":null,"language":"JavaScript","languageID":183,"large":false,"loggedIn":false,"planSupportInfo":{"repoIsFork":null,"repoOwnedByCurrentUser":null,"requestFullPath":"/Ichrafsassi/alx-higher_level_programming/blob/master/0x15-javascript-web_jquery/8-script.js","showFreeOrgGatedFeatureMessage":null,"showPlanSupportBanner":null,"upgradeDataAttributes":null,"upgradePath":null},"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_dockerfile","releasePath":"/Ichrafsassi/alx-higher_level_programming/releases/new?marketplace=true","showPublishActionBanner":false},"rawBlobUrl":"https://github.com/Ichrafsassi/alx-higher_level_programming/raw/master/0x15-javascript-web_jquery/8-script.js","renderImageOrRaw":false,"richText":null,"renderedFileInfo":null,"shortPath":null,"symbolsEnabled":true,"tabSize":8,"topBannersInfo":{"overridingGlobalFundingFile":false,"globalPreferredFundingPath":null,"repoOwner":"Ichrafsassi","repoName":"alx-higher_level_programming","showInvalidCitationWarning":false,"citationHelpUrl":"https://docs.github.com/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files","actionsOnboardingTip":null},"truncated":false,"viewable":true,"workflowRedirectUrl":null,"symbols":{"timed_out":false,"not_analyzed":false,"symbols":[]}},"copilotInfo":null,"copilotAccessAllowed":false,"csrf_tokens":{"/Ichrafsassi/alx-higher_level_programming/branches":{"post":"SQcKlSUxAP-0Sy3wzYcPcpgu0son7NxXs-7jZmgkMizoaw4iU5FB9ow6CyIw4-2jB-S7OHkbDSv1q1Id4Spvog"},"/repos/preferences":{"post":"__R7p6CI30S_LMgZfMJUir2QrKUh0pK5wZDqLQigK2RaJoOM-TvaNVqeW6gG5Ei2cMr4tw6HYW56knAE1Y-phQ"}}},"title":"alx-higher_level_programming/0x15-javascript-web_jquery/8-script.js at master · Ichrafsassi/alx-higher_level_programming"}