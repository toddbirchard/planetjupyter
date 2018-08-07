
$(document).ready(function(){var api_url='https://api.linkpreview.net/';base_external_url='https://api.plot.ly/v2/jupyter-notebooks/external?source='
function verifyImage(input){if(input.length>0){return'<div class="preview-image" style="background-image:url('+input+');"></div>'}else{return"";}}
function verifyTitle(input){if(input.title==""){return input.url;}else{return input.title;}}
function postLinkPreviews(){$('a').each(function(index,element){var target=$(this).attr('href')
$.ajax({url:api_url+"?key=5b439c179073fae7b9928e83dc64e969bd01b9562d693&q="+$(this).text(),contentType:"application/json",dataType:'json',success:function(result){var link_image=verifyImage(result.image);var verify_title=verifyTitle(result);console.log(result);$(element).after('<a href="#" onclick="loadRecent('+target+')"><div class="link-preview">'+link_image+'<div class="link-info"><h4>'+verify_title+'</h4><p>'+result.description+'</p></div></div></a>');$("a").click(function(event){event.preventDefault();$('input').val(target);$("form").submit();});$(element).remove();});});});}
postLinkPreviews();});