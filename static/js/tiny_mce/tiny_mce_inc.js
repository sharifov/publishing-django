function mce_filebrowser(field_name, url, type, win) {
    //document.domain = SETTINGS.get("DOCUMENT_DOMAIN");//this is to allow cross subdomain loading of popups
    tinyMCE.activeEditor.windowManager.open({
        url: "/filebrowser/" + type + "/",
        title: 'Insert media',
        width: 550,
        height: 300
    }, {
        window : win,
        input : field_name
    });  
}

tinyMCE.init({
		// General options
		mode : "textareas",
		width:'80%',
		height:450,
		//mode : "specific_textareas",
		//editor_selector : "jeditor",
		theme : "advanced",
		file_browser_callback : "mce_filebrowser",
		skin : "o2k7",
		skin_variant : "silver",
		relative_urls : false,
		convert_urls: false,
		remove_script_host : false,
		plugins : "autolink,lists,pagebreak,style,layer,table,save,advhr,advimage,advlink,emotions,iespell,insertdatetime,preview,media,searchreplace,print,contextmenu,paste,directionality,fullscreen,noneditable,visualchars,nonbreaking,xhtmlxtras,template,inlinepopups,autosave",
		
		theme_advanced_styles : "Sari yazi=sari",
		
		// Theme options
		theme_advanced_buttons1 : "save,newdocument,|,bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,|,styleselect,formatselect,fontselect,fontsizeselect",
		theme_advanced_buttons2 : "pasteword,|,search,replace,|,bullist,numlist,|,outdent,indent|,undo,redo,|,link,unlink,image,code,|,insertdate,inserttime,preview,|,forecolor,backcolor",
		theme_advanced_buttons3 : "tablecontrols,|,hr,removeformat,visualaid,|,sub,sup,|,charmap,emotions,iespell,media,advhr,|,print,|,fullscreen",
		theme_advanced_buttons4 : "styleprops,|,cite,abbr,acronym,del,ins,|,pagebreak",
		theme_advanced_toolbar_location : "top",
		theme_advanced_toolbar_align : "left",
		theme_advanced_statusbar_location : "bottom",
		theme_advanced_resizing : true,

		// Example word content CSS (should be your site CSS) this one removes paragraph margins
		content_css : "css/word.css",

		// Drop lists for link/image/media/template dialogs
		template_external_list_url : "../tiny_mce/lists/template_list.js",
		external_link_list_url : "../tiny_mce/lists/link_list.js",
		media_external_list_url : "../tiny_mce/lists/media_list.js",

		// Replace values for the template plugin
		template_replace_values : {
			username : "Some User",
			staffid : "991234"
		}
	});