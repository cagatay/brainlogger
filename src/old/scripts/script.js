$('.editButton').click( function(){
  var a = $(this)
  var e = a.parent().next();
  if(e.attr('contenteditable') == 'true'){
    e.attr('contenteditable', 'false');
    e.css('border', 'none');
    a.val('edit');
    var param = [e.attr('id'), e.html()];
    Request('editEntry', param);
  }
  else{
    e.attr('contenteditable', 'true'); 
    e.css('border', '2px dotted');
    //localStorage.setItem(e.attr('id'), e.html())
    a.val('ok');
    e.focus();
  }
  });

function showForm(){
  var e = document.getElementById("entryform");
  var a = document.getElementById("formbutton");
  if(a.value == 'write'){
    e.style.display = 'block';
    a.value = 'discard'; 
  }
  else{
    e.style.display = 'none';
    a.value = 'write';
  }
}

function Request(function_name, opt_argv) {

  if (!opt_argv)
    opt_argv = new Array();

  // Find if the last arg is a callback function; save it
  var callback = null;
  var len = opt_argv.length;
  if (len > 0 && typeof opt_argv[len-1] == 'function') {
    callback = opt_argv[len-1];
    opt_argv.length--;
  }
  var async = (callback != null);

  // Build an Array of parameters, w/ function_name being the first parameter
  var params = new Array(function_name);
  for (var i = 0; i < opt_argv.length; i++) {
    params.push(opt_argv[i]);
  }
  var body = JSON.stringify(params);

  // Create an XMLHttpRequest 'POST' request w/ an optional callback handler
  var req = new XMLHttpRequest();
  req.open('POST', '/rpc', async);

  req.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

  if (async) {
    req.onreadystatechange = function() {
      if(req.readyState == 4 && req.status == 200) {
        var response = null;
        try {
         response = JSON.parse(req.responseText);
        } catch (e) {
         response = req.responseText;
        }
        callback(response);
      }
    }
  }

  // Make the actual request
  req.send(body);
  eval(req.responseText);
}

