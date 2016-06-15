$(document).ready(function(){
    $(".dropdown").hover(            
        function() {
            $('.dropdown-menu', this).stop( true, true ).slideDown("fast");
            $(this).toggleClass('open');        
        },
        function() {
            $('.dropdown-menu', this).stop( true, true ).slideUp("fast");
            $(this).toggleClass('open');       
        }
    );
});

(function() {
// trim polyfill : https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/Trim
if (!String.prototype.trim) {
  (function() {
    // Make sure we trim BOM and NBSP
    var rtrim = /^[\s\uFEFF\xA0]+|[\s\uFEFF\xA0]+$/g;
    String.prototype.trim = function() {
      return this.replace(rtrim, '');
    };
  })();
}

[].slice.call( document.querySelectorAll( 'input.input__field' ) ).forEach( function( inputEl ) {
  // in case the input is already filled..
  if( inputEl.value.trim() !== '' ) {
    classie.add( inputEl.parentNode, 'input--filled' );
  }

  // events:
  inputEl.addEventListener( 'focus', onInputFocus );
  inputEl.addEventListener( 'blur', onInputBlur );
} );

function onInputFocus( ev ) {
  classie.add( ev.target.parentNode, 'input--filled' );
}

function onInputBlur( ev ) {
  if( ev.target.value.trim() === '' ) {
    classie.remove( ev.target.parentNode, 'input--filled' );
  }
}
})();


function start() {
  Check11();
  Check12();
}
window.onload = start;

function Check11() {
         
    
    if (document.getElementById("category").value == "All_type"){ 
        document.getElementById('all_things').style.display = 'block';
        document.getElementById('Телефоны').style.display = 'none';
        document.getElementById('Ноутбуки').style.display = 'none';
        document.getElementById('Планшеты').style.display = 'none';
        document.getElementById('Аксессуары').style.display = 'none';
        
    }
    if (document.getElementById("category").value == "Телефоны"){ 
        document.getElementById('Телефоны').style.display = 'block';
        document.getElementById('Ноутбуки').style.display = 'none';
        document.getElementById('Планшеты').style.display = 'none';
        document.getElementById('all_things').style.display = 'none';
        document.getElementById('Аксессуары').style.display = 'none';
        
    }
    if (document.getElementById("category").value == "Ноутбуки"){
        document.getElementById('Телефоны').style.display = 'none';
        document.getElementById('Ноутбуки').style.display = 'block';
        document.getElementById('Планшеты').style.display = 'none';
        document.getElementById('all_things').style.display = 'none';
        document.getElementById('Аксессуары').style.display = 'none';

       
    }
    if (document.getElementById("category").value == "Планшеты"){
        document.getElementById('Телефоны').style.display = 'none';
        document.getElementById('Ноутбуки').style.display = 'none';
        document.getElementById('Планшеты').style.display = 'block';
        document.getElementById('all_things').style.display = 'none';
        document.getElementById('Аксессуары').style.display = 'none';
        
    }
    if (document.getElementById("category").value == "Аксессуары"){
        document.getElementById('Телефоны').style.display = 'none';
        document.getElementById('Ноутбуки').style.display = 'none';
        document.getElementById('Аксессуары').style.display = 'block';
        document.getElementById('all_things').style.display = 'none';
        document.getElementById('Планшеты').style.display = 'none';
        
    }
}


function Check12() {
    
    if (document.getElementById("category_m").value == "All_type"){ 
        document.getElementById('all_things_m').style.display = 'block';
        document.getElementById('Телефоны_m').style.display = 'none';
        document.getElementById('Ноутбуки_m').style.display = 'none';
        document.getElementById('Планшеты_m').style.display = 'none';
        document.getElementById('Аксессуары_m').style.display = 'none';
    }
    if (document.getElementById("category_m").value == "Телефоны"){ 
        document.getElementById('Телефоны_m').style.display = 'block';
        document.getElementById('Ноутбуки_m').style.display = 'none';
        document.getElementById('Планшеты_m').style.display = 'none';
        document.getElementById('all_things_m').style.display = 'none';
        document.getElementById('Аксессуары_m').style.display = 'none';
        
    }
    if (document.getElementById("category_m").value == "Ноутбуки"){
        document.getElementById('Телефоны_m').style.display = 'none';
        document.getElementById('Ноутбуки_m').style.display = 'block';
        document.getElementById('Планшеты_m').style.display = 'none';
        document.getElementById('all_things_m').style.display = 'none';
        document.getElementById('Аксессуары_m').style.display = 'none';

       
    }
    if (document.getElementById("category_m").value == "Планшеты"){
        document.getElementById('Телефоны_m').style.display = 'none';
        document.getElementById('Ноутбуки_m').style.display = 'none';
        document.getElementById('Планшеты_m').style.display = 'block';
        document.getElementById('all_things_m').style.display = 'none';
        document.getElementById('Аксессуары_m').style.display = 'none';
        
    }
    if (document.getElementById("category_m").value == "Аксессуары"){
        document.getElementById('Аксессуары_m').style.display = 'block';
        document.getElementById('Телефоны_m').style.display = 'none';
        document.getElementById('Ноутбуки_m').style.display = 'none';
        document.getElementById('Планшеты_m').style.display = 'none';
        document.getElementById('all_things_m').style.display = 'none';
        
    }
}
