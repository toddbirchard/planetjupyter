$( document ).ready(function() {
  $('base').attr('href', 'https://planetjupyter.com/');

  $('.rendered_html table').css('width', '100% !important');
  $('.rendered_html table').css('margin', 'auto !important');

  $('div.output_area img').css('max-width', '90%');
  $('div.output_subarea').css('text-align', 'center');
  $('output_png output_subarea').css('text-align', 'center');

  $('.rendered_html p').css('font-family', 'Whitney SSm A, Whitney SSm B !important');
  $('li').css('font-family', 'Whitney SSm A, Whitney SSm B !important');
  $('.rendered_html p').css('weight', 'normal');
  $('.rendered_html p').css('font-size', '1.85rem');
  $('.rendered_html p').css('font-size', '400');

  $('.rendered_html h1').css('font-family', 'Whitney SSm A, Whitney SSm B !important');
  $('.rendered_html h1').css('font-size', '2.5em');
  $('.rendered_html h1').css('line-height', '1');
  $('.rendered_html h1').css('fborder-bottom', '1px solid #e3e3e3');
  $('.rendered_html h1').css('padding-bottom', '20px');
  $('.rendered_html h1').css('font-weight', 'bold');
  $('.rendered_html h1').css('margin', '1.08em 0 0');
  $('.rendered_html h1').css('font-size', '400');

  $('.rendered_html h2').css('font-family', 'montserrat !important');
  $('.rendered_html h2').css('font-size', '2.5em  !important');
  $('.rendered_html h2').css('line-height', '1');
  $('.rendered_html h2').css('border-bottom', '1px solid #e3e3e3');
  $('.rendered_html h2').css('padding-bottom', '20px');
  $('.rendered_html h2').css('font-weight', 'bold ! !important');
  $('.rendered_html h2').css('margin', '3rem 0 1.75rem ! !important');
  $('.rendered_html h2').css('font-size', '400 !important');
  $('.rendered_html h2').css('color', '#0F9B85 !important');
  $('.rendered_html h2').css('text-transform:', 'none');

  $('div#notebook-container').css('max-width', '1100px');
  $('div#notebook-container').css('padding', '40px !important');

  $('.rendered_html table').css('width', '90%');
});
