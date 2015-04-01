Twitch.init({clientId: 'atvcz912gs1lphwey76fyzfb8wtnru8'}, function(error, status) {
	if (error) {
		// error encountered while loading
		console.log(error);
	}
	// the sdk is now loaded
	if (status.authenticated) {
		// user is currently logged in
	}

	$(function () {
		window.onPlayerEvent = function (data) {
			data.forEach(function(event) {
				if (event.event == "playerInit") {
					var player = $("#live_embed_player")[0];
					player.playVideo();
					player.mute();
				}
			});
		}

		swfobject.embedSWF("http://www-cdn.jtvnw.net/swflibs/TwitchPlayer.swf", "twitch_embed_player", "650", "400", "11", null,
			{ "eventsCallback":"onPlayerEvent",
			"embed":1,
			"channel":"mic_feedback",
			"auto_play":"true"},
			{ "allowScriptAccess":"always",
			"allowFullScreen":"true"});
	});
});