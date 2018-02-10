$(function(){
  var title = $('#console-title').text();
  $(".console-title").typed({
    strings: [title],
    typeSpeed: -100,
    callback: function(){
      $('.console-input').focus();
    }
  });
});
var output = $('.console-output');
var input = $('.console-input');
var path = $('.console-path');
var ps1 = $('.console-ps1');
input.keypress(function(e) {
  if (e.which == 13) {
    var inputVal = $.trim(input.val());
    addPs1();
    if (inputVal == 'help') {
      help();
      input.val('');
    } else if (inputVal == 'about') {
      aboutMe();
      input.val('');
    } else if (inputVal == 'whoami') {
      aboutMe();
      input.val('');
    } else if (inputVal == 'contact') {
      contactMe();
      input.val('');
    } else if (inputVal == 'date') {
      getTime();
      input.val('');
    } else if (inputVal == 'clear') {
      clearConsole();
      input.val('');
    } else if (inputVal.startsWith('cd') === true) {
      cdPath(inputVal);
      input.val('');
    } else if (inputVal == '') {
      input.val('');
    } else {
      Output('<span>' + 'bash: ' +  inputVal + ': command not found</span></br>');
      input.val('');
    }
  }
});

function help() {
  var commandsArray = [
    'Help: List of available commands',
    '>help',
    '>cd',
    '>about',
    '>whoami',
    '>contact',
    '>date',
    '>clear'
  ];
  for (var i = 0; i < commandsArray.length; i++) {
    var out = '<span>' + commandsArray[i] + '</span><br/>';
    Output(out);
  }
};
function clearConsole() {
  output.html('');
  Output('<span>clear</span></br>');
}
function getTime() {
  Output('<span>It\'s the 21st century man! Get a SmartWatch</span></br>');
}
function aboutMe() {
  var aboutMeArray = [
    '>About:',
    'Hello!',
    'MY NAME IS HONMAPLE.',
    'Welcome to MY Website'
  ];
  for (var i = 0; i < aboutMeArray.length; i++) {
    var out = '<span>' + aboutMeArray[i] + '</span><br/>';
    Output(out);
  }
}
function contactMe() {
  var contactArray = [
    '>Contact:<br/>',
    '<a href="https://github.com/honmaple" target="_blank" title="GitHub"><i class="fa fa-github" aria-hidden="true"></i></a>',
    '<a href="https://honmaple.com/blog/" target="_blank" title="Blog"><i class="fa fa-leaf" aria-hidden="true"></i></a>',
    '<a href="https://honmaple.com/books/" target="_blank" title="Book"><i class="fa fa-book" aria-hidden="true"></i></a>',
    '<a href="http://weibo.com/honmaple" target="_blank" title="WeiBo"><i class="fa fa-weibo" aria-hidden="true"></i></a>',
    '<a href="xiyang0807@gmail.com" target="_blank" title="Gmail"><i class="fa fa-envelope" aria-hidden="true"></i></a>',
  ];
  for (var i = 0; i < contactArray.length; i++) {
    var out = '<span>' + contactArray[i] + '</span>';
    Output(out);
  }
  Output('<br/>')
}
function cdPath(data) {
  data = data.substr(data.indexOf(' ') + 1);
  if (data == 'cd' || data == '~/' || data == '~') {
    path.text('~');
  } else if (data.startsWith('~') === true) {
    path.text(data);
  } else if (data == 'blog' || data == 'book') {
    path.text(path.text() + '/' + data);
  } else {
    Output('<span>' + 'bash: cd: ' + data + ': No such file or directory' + '</span></br>');
  };
}
function addPs1() {
  Output('<span>' + ps1.html() + '</span></br>');
}
function seperator() {
  Output('<span class="seperator">== == == == == == == == == == == == == == == == == ==</span></br>');
}
function Output(data) {
  $(data).appendTo(output);
}
