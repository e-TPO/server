$(document).ready(function(){
	$("#notice_display_div").marquee();
	$.get({
		url : '/api/v1.0/get_notice',
		method : 'GET',
		success : function(data){
					if(data.success == true){
						var list = "";
						for(i in data.data){
							list += "<li>"+ data.data[i]['title'] +"</li>";
						}
						$("#notice_display_div").html(list);
						// $("#notice_display_div").marquee({
						// 	//duration in milliseconds of the marquee
						// 	duration: 15000,
						// 	//gap in pixels between the tickers
						// 	gap: 10,
						// 	//time in milliseconds before the marquee will start animating
						// 	delayBeforeStart: 0,
						// 	//'left' or 'right'
						// 	direction: 'left',
						// 	//true or false - should the marquee be duplicated to show an effect of continues flow
						// 	duplicated: true
						// });
						console.log(data.data);
					}
				},
		error : function(){
			alert("An error occured!");
				}
	});
});