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
  Check_phones();
  Check_notebooks();
  Check_tablets();
  Check_accessories();
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





function Check2() {
    if (document.getElementById('category_id').value == "" ){
        document.getElementById('category_id').value = 0;
    }
    document.getElementById('brand_id').value = document.getElementById('category_id').value;
};

function Check_sum() {
    if (document.getElementById('sum').value == "" ){
        document.getElementById('sum').value = 0;
    }
    document.getElementById('price').value = document.getElementById('sum').value;
};

function Check_sum_notify() {
    if (document.getElementById('from_notifyp').value == "" ){
        document.getElementById('from_notifyp').value = 0;
    }
    document.getElementById('from_notify').value = document.getElementById('from_notifyp').value;
    if (document.getElementById('to_notifyp').value == "" ){
        document.getElementById('to_notifyp').value = 0;
    }
    document.getElementById('to_notify').value = document.getElementById('to_notifyp').value;
};

function Check_fun() {
    var mod = document.getElementById("Apple_second").value;
    var mod1 = document.getElementById("Samsung_second").value;
    var mod2 = document.getElementById("Sony_second").value;
    var mod3 = document.getElementById("Nokia_second").value;
    var mod4 = document.getElementById("LG_second").value;
    var mod5 = document.getElementById("BlackBerry_second").value;
    var mod6 = document.getElementById("Lenovo_second").value;
    var mod7 = document.getElementById("HTC_second").value;
    var mod8 = document.getElementById("Huawei_second").value;
    var mod9 = document.getElementById("Microsoft_second").value;
    var mod10 = document.getElementById("Asus_second").value;
    var mod11 = document.getElementById("OnePlus_second").value;
    var mod12 = document.getElementById("Другие бренды_second").value;
    mod = mod.split("_");
    if (document.getElementById("brand").value == "Apple" && mod.length == 2){
        document.getElementById('Apple_first').style.display = 'block';

    }
    else{
        document.getElementById('Apple_first').style.display = 'none';
    }
    mod1 = mod1.split("_");
    if (document.getElementById("brand").value == "Samsung" && mod1.length == 2){
        document.getElementById('Samsung_first').style.display = 'block';
    }
    else{
        document.getElementById('Samsung_first').style.display = 'none';
    }
    mod2 = mod2.split("_");
    if (document.getElementById("brand").value == "Sony" && mod2.length == 2){
        document.getElementById('Sony_first').style.display = 'block';
    }
    else{
        document.getElementById('Sony_first').style.display = 'none';
    }
    mod3 = mod3.split("_");
    if (document.getElementById("brand").value == "Nokia" && mod3.length == 2){
        document.getElementById('Nokia_first').style.display = 'block';
    }
    else{
        document.getElementById('Nokia_first').style.display = 'none';
    }
    mod4 = mod4.split("_");
    if (document.getElementById("brand").value == "LG" && mod4.length == 2){
        document.getElementById('LG_first').style.display = 'block';
    }
    else{
        document.getElementById('LG_first').style.display = 'none';
    }
    mod5 = mod5.split("_");
    if (document.getElementById("brand").value == "BlackBerry" && mod5.length == 2){
        document.getElementById('BlackBerry_first').style.display = 'block';
    }
    else{
        document.getElementById('BlackBerry_first').style.display = 'none';
    }
    mod6 = mod6.split("_");
    if (document.getElementById("brand").value == "Lenovo" && mod6.length == 2){
        document.getElementById('Lenovo_first').style.display = 'block';
    }
    else{
        document.getElementById('Lenovo_first').style.display = 'none';
    }
    mod7 = mod7.split("_");
    if (document.getElementById("brand").value == "HTC" && mod7.length == 2){
        document.getElementById('HTC_first').style.display = 'block';
    }
    else{
        document.getElementById('HTC_first').style.display = 'none';
    }
    mod8 = mod8.split("_");
    if (document.getElementById("brand").value == "Huawei" && mod8.length == 2){
        document.getElementById('Huawei_first').style.display = 'block';
    }
    else{
        document.getElementById('Huawei_first').style.display = 'none';
    }
    mod9 = mod9.split("_");
    if (document.getElementById("brand").value == "Microsoft" && mod9.length == 2){
        document.getElementById('Microsoft_first').style.display = 'block';
    }
    else{
        document.getElementById('Microsoft_first').style.display = 'none';
    }
    mod10 = mod10.split("_");
    if (document.getElementById("brand").value == "Asus" && mod10.length == 2){
        document.getElementById('Asus_first').style.display = 'block';
    }
    else{
        document.getElementById('Asus_first').style.display = 'none';
    }
    mod11 = mod11.split("_");
    if (document.getElementById("brand").value == "OnePlus" && mod11.length == 2){
        document.getElementById('OnePlus_first').style.display = 'block';
    }
    else{
        document.getElementById('OnePlus_first').style.display = 'none';
    }
    mod12 = mod12.split("_");
    if (document.getElementById("brand").value == "Другие бренды" && mod12.length == 2){
        document.getElementById('Другие бренды_first').style.display = 'block';
    }
    else{
        document.getElementById('Другие бренды_first').style.display = 'none';
    }
}

function Check_phones() {
    if (document.getElementById("brand").value == "Apple"){
        document.getElementById('Apple').style.display = 'block';
        document.getElementById('Samsung').style.display = 'none';
        document.getElementById('Sony').style.display = 'none';
        document.getElementById('Nokia').style.display = 'none';
        document.getElementById('LG').style.display = 'none';
        document.getElementById('BlackBerry').style.display = 'none';
        document.getElementById('Lenovo').style.display = 'none';
        document.getElementById('HTC').style.display = 'none';
        document.getElementById('Huawei').style.display = 'none';
        document.getElementById('Microsoft').style.display = 'none';
        document.getElementById('Другие бренды').style.display = 'none';
        document.getElementById('Asus').style.display = 'none';
        document.getElementById('OnePlus').style.display = 'none';
    }
    if (document.getElementById("brand").value == "Microsoft"){
        document.getElementById('Microsoft').style.display = 'block';
        document.getElementById('Samsung').style.display = 'none';
        document.getElementById('Apple').style.display = 'none';
        document.getElementById('Sony').style.display = 'none';
        document.getElementById('Nokia').style.display = 'none';
        document.getElementById('LG').style.display = 'none';
        document.getElementById('BlackBerry').style.display = 'none';
        document.getElementById('Lenovo').style.display = 'none';
        document.getElementById('HTC').style.display = 'none';
        document.getElementById('Huawei').style.display = 'none';
        document.getElementById('Другие бренды').style.display = 'none';
        document.getElementById('Asus').style.display = 'none';
        document.getElementById('OnePlus').style.display = 'none';
    }
    if (document.getElementById("brand").value == "Huawei"){
        document.getElementById('Huawei').style.display = 'block';
        document.getElementById('HTC').style.display = 'none';
        document.getElementById('Samsung').style.display = 'none';
        document.getElementById('Apple').style.display = 'none';
        document.getElementById('Sony').style.display = 'none';
        document.getElementById('Nokia').style.display = 'none';
        document.getElementById('LG').style.display = 'none';
        document.getElementById('BlackBerry').style.display = 'none';
        document.getElementById('Lenovo').style.display = 'none';
        document.getElementById('Microsoft').style.display = 'none';
        document.getElementById('Другие бренды').style.display = 'none';
        document.getElementById('Asus').style.display = 'none';
        document.getElementById('OnePlus').style.display = 'none';
    }
    if (document.getElementById("brand").value == "HTC"){
        document.getElementById('HTC').style.display = 'block';
        document.getElementById('Samsung').style.display = 'none';
        document.getElementById('Apple').style.display = 'none';
        document.getElementById('Sony').style.display = 'none';
        document.getElementById('Nokia').style.display = 'none';
        document.getElementById('LG').style.display = 'none';
        document.getElementById('BlackBerry').style.display = 'none';
        document.getElementById('Lenovo').style.display = 'none';
        document.getElementById('Huawei').style.display = 'none';
        document.getElementById('Microsoft').style.display = 'none';
        document.getElementById('Другие бренды').style.display = 'none';
        document.getElementById('Asus').style.display = 'none';
        document.getElementById('OnePlus').style.display = 'none';
    }
    if (document.getElementById("brand").value == "Lenovo"){
        document.getElementById('Lenovo').style.display = 'block';
        document.getElementById('Samsung').style.display = 'none';
        document.getElementById('Sony').style.display = 'none';
        document.getElementById('Nokia').style.display = 'none';
        document.getElementById('LG').style.display = 'none';
        document.getElementById('BlackBerry').style.display = 'none';
        document.getElementById('Apple').style.display = 'none';
        document.getElementById('HTC').style.display = 'none';
        document.getElementById('Huawei').style.display = 'none';
        document.getElementById('Microsoft').style.display = 'none';
        document.getElementById('Другие бренды').style.display = 'none';
        document.getElementById('Asus').style.display = 'none';
        document.getElementById('OnePlus').style.display = 'none';
    }
    if (document.getElementById("brand").value == "BlackBerry"){
        document.getElementById('BlackBerry').style.display = 'block';
        document.getElementById('Samsung').style.display = 'none';
        document.getElementById('Apple').style.display = 'none';
        document.getElementById('Sony').style.display = 'none';
        document.getElementById('Nokia').style.display = 'none';
        document.getElementById('LG').style.display = 'none';
        document.getElementById('Lenovo').style.display = 'none';
        document.getElementById('HTC').style.display = 'none';
        document.getElementById('Huawei').style.display = 'none';
        document.getElementById('Microsoft').style.display = 'none';
        document.getElementById('Другие бренды').style.display = 'none';
        document.getElementById('Asus').style.display = 'none';
        document.getElementById('OnePlus').style.display = 'none';
    }
    if (document.getElementById("brand").value == "Samsung") {
        document.getElementById('Samsung').style.display = 'block';
        document.getElementById('Apple').style.display = 'none';
        document.getElementById('Sony').style.display = 'none';
        document.getElementById('Nokia').style.display = 'none';
        document.getElementById('LG').style.display = 'none';
        document.getElementById('BlackBerry').style.display = 'none';
        document.getElementById('Lenovo').style.display = 'none';
        document.getElementById('HTC').style.display = 'none';
        document.getElementById('Huawei').style.display = 'none';
        document.getElementById('Microsoft').style.display = 'none';
        document.getElementById('Другие бренды').style.display = 'none';
        document.getElementById('Asus').style.display = 'none';
        document.getElementById('OnePlus').style.display = 'none';
    }
    if (document.getElementById("brand").value == "Nokia") {
        document.getElementById('Nokia').style.display = 'block';
        document.getElementById('Apple').style.display = 'none';
        document.getElementById('Samsung').style.display = 'none';
        document.getElementById('Sony').style.display = 'none';
        document.getElementById('LG').style.display = 'none';
        document.getElementById('BlackBerry').style.display = 'none';
        document.getElementById('Lenovo').style.display = 'none';
        document.getElementById('HTC').style.display = 'none';
        document.getElementById('Huawei').style.display = 'none';
        document.getElementById('Microsoft').style.display = 'none';
        document.getElementById('Другие бренды').style.display = 'none';
        document.getElementById('Asus').style.display = 'none';
        document.getElementById('OnePlus').style.display = 'none';
    }

    if (document.getElementById("brand").value == "Sony") {
        document.getElementById('Sony').style.display = 'block';
        document.getElementById('Apple').style.display = 'none';
        document.getElementById('Samsung').style.display = 'none';
        document.getElementById('Nokia').style.display = 'none';
        document.getElementById('LG').style.display = 'none';
        document.getElementById('BlackBerry').style.display = 'none';
        document.getElementById('Lenovo').style.display = 'none';
        document.getElementById('HTC').style.display = 'none';
        document.getElementById('Huawei').style.display = 'none';
        document.getElementById('Microsoft').style.display = 'none';
        document.getElementById('Другие бренды').style.display = 'none';
        document.getElementById('Asus').style.display = 'none';
        document.getElementById('OnePlus').style.display = 'none';
    }
    if (document.getElementById("brand").value == "LG"){
        document.getElementById('LG').style.display = 'block';
        document.getElementById('Apple').style.display = 'none';
        document.getElementById('Samsung').style.display = 'none';
        document.getElementById('Sony').style.display = 'none';
        document.getElementById('Nokia').style.display = 'none';
        document.getElementById('BlackBerry').style.display = 'none';
        document.getElementById('Lenovo').style.display = 'none';
        document.getElementById('HTC').style.display = 'none';
        document.getElementById('Huawei').style.display = 'none';
        document.getElementById('Microsoft').style.display = 'none';
        document.getElementById('Другие бренды').style.display = 'none';
        document.getElementById('Asus').style.display = 'none';
        document.getElementById('OnePlus').style.display = 'none';
    }
    if (document.getElementById("brand").value == "Другие бренды"){
        document.getElementById('LG').style.display = 'none';
        document.getElementById('Apple').style.display = 'none';
        document.getElementById('Samsung').style.display = 'none';
        document.getElementById('Sony').style.display = 'none';
        document.getElementById('Nokia').style.display = 'none';
        document.getElementById('BlackBerry').style.display = 'none';
        document.getElementById('Lenovo').style.display = 'none';
        document.getElementById('HTC').style.display = 'none';
        document.getElementById('Huawei').style.display = 'none';
        document.getElementById('Microsoft').style.display = 'none';
        document.getElementById('Другие бренды').style.display = 'block';
        document.getElementById('Asus').style.display = 'none';
        document.getElementById('OnePlus').style.display = 'none';
    }
    if (document.getElementById("brand").value == "Asus"){
        document.getElementById('LG').style.display = 'none';
        document.getElementById('Apple').style.display = 'none';
        document.getElementById('Samsung').style.display = 'none';
        document.getElementById('Sony').style.display = 'none';
        document.getElementById('Nokia').style.display = 'none';
        document.getElementById('BlackBerry').style.display = 'none';
        document.getElementById('Lenovo').style.display = 'none';
        document.getElementById('HTC').style.display = 'none';
        document.getElementById('Huawei').style.display = 'none';
        document.getElementById('Microsoft').style.display = 'none';
        document.getElementById('Другие бренды').style.display = 'none';
        document.getElementById('Asus').style.display = 'block';
        document.getElementById('OnePlus').style.display = 'none';
    }
    if (document.getElementById("brand").value == "OnePlus"){
        document.getElementById('LG').style.display = 'none';
        document.getElementById('Apple').style.display = 'none';
        document.getElementById('Samsung').style.display = 'none';
        document.getElementById('Sony').style.display = 'none';
        document.getElementById('Nokia').style.display = 'none';
        document.getElementById('BlackBerry').style.display = 'none';
        document.getElementById('Lenovo').style.display = 'none';
        document.getElementById('HTC').style.display = 'none';
        document.getElementById('Huawei').style.display = 'none';
        document.getElementById('Microsoft').style.display = 'none';
        document.getElementById('Другие бренды').style.display = 'none';
        document.getElementById('Asus').style.display = 'none';
        document.getElementById('OnePlus').style.display = 'block';
    }
}

function Check_tablets() {
    if (document.getElementById("brand").value == "Apple"){
        document.getElementById('Apple').style.display = 'block';
        document.getElementById('Samsung').style.display = 'none';
        document.getElementById('Sony').style.display = 'none';
        document.getElementById('Nokia').style.display = 'none';
        document.getElementById('LG').style.display = 'none';
        document.getElementById('BlackBerry').style.display = 'none';
        document.getElementById('Lenovo').style.display = 'none';
        document.getElementById('HTC').style.display = 'none';
        document.getElementById('Huawei').style.display = 'none';
        document.getElementById('Microsoft').style.display = 'none';
        document.getElementById('Другие бренды').style.display = 'none';
        document.getElementById('Asus').style.display = 'none';
    }
    if (document.getElementById("brand").value == "Microsoft"){
        document.getElementById('Microsoft').style.display = 'block';
        document.getElementById('Samsung').style.display = 'none';
        document.getElementById('Apple').style.display = 'none';
        document.getElementById('Sony').style.display = 'none';
        document.getElementById('Nokia').style.display = 'none';
        document.getElementById('LG').style.display = 'none';
        document.getElementById('BlackBerry').style.display = 'none';
        document.getElementById('Lenovo').style.display = 'none';
        document.getElementById('HTC').style.display = 'none';
        document.getElementById('Huawei').style.display = 'none';
        document.getElementById('Другие бренды').style.display = 'none';
        document.getElementById('Asus').style.display = 'none';
    }
    if (document.getElementById("brand").value == "Huawei"){
        document.getElementById('Huawei').style.display = 'block';
        document.getElementById('HTC').style.display = 'none';
        document.getElementById('Samsung').style.display = 'none';
        document.getElementById('Apple').style.display = 'none';
        document.getElementById('Sony').style.display = 'none';
        document.getElementById('Nokia').style.display = 'none';
        document.getElementById('LG').style.display = 'none';
        document.getElementById('BlackBerry').style.display = 'none';
        document.getElementById('Lenovo').style.display = 'none';
        document.getElementById('Microsoft').style.display = 'none';
        document.getElementById('Другие бренды').style.display = 'none';
        document.getElementById('Asus').style.display = 'none';
    }
    if (document.getElementById("brand").value == "HTC"){
        document.getElementById('HTC').style.display = 'block';
        document.getElementById('Samsung').style.display = 'none';
        document.getElementById('Apple').style.display = 'none';
        document.getElementById('Sony').style.display = 'none';
        document.getElementById('Nokia').style.display = 'none';
        document.getElementById('LG').style.display = 'none';
        document.getElementById('BlackBerry').style.display = 'none';
        document.getElementById('Lenovo').style.display = 'none';
        document.getElementById('Huawei').style.display = 'none';
        document.getElementById('Microsoft').style.display = 'none';
        document.getElementById('Другие бренды').style.display = 'none';
        document.getElementById('Asus').style.display = 'none';
    }
    if (document.getElementById("brand").value == "Lenovo"){
        document.getElementById('Lenovo').style.display = 'block';
        document.getElementById('Samsung').style.display = 'none';
        document.getElementById('Sony').style.display = 'none';
        document.getElementById('Nokia').style.display = 'none';
        document.getElementById('LG').style.display = 'none';
        document.getElementById('BlackBerry').style.display = 'none';
        document.getElementById('Apple').style.display = 'none';
        document.getElementById('HTC').style.display = 'none';
        document.getElementById('Huawei').style.display = 'none';
        document.getElementById('Microsoft').style.display = 'none';
        document.getElementById('Другие бренды').style.display = 'none';
        document.getElementById('Asus').style.display = 'none';
    }
    if (document.getElementById("brand").value == "BlackBerry"){
        document.getElementById('BlackBerry').style.display = 'block';
        document.getElementById('Samsung').style.display = 'none';
        document.getElementById('Apple').style.display = 'none';
        document.getElementById('Sony').style.display = 'none';
        document.getElementById('Nokia').style.display = 'none';
        document.getElementById('LG').style.display = 'none';
        document.getElementById('Lenovo').style.display = 'none';
        document.getElementById('HTC').style.display = 'none';
        document.getElementById('Huawei').style.display = 'none';
        document.getElementById('Microsoft').style.display = 'none';
        document.getElementById('Другие бренды').style.display = 'none';
        document.getElementById('Asus').style.display = 'none';
    }
    if (document.getElementById("brand").value == "Samsung") {
        document.getElementById('Samsung').style.display = 'block';
        document.getElementById('Apple').style.display = 'none';
        document.getElementById('Sony').style.display = 'none';
        document.getElementById('Nokia').style.display = 'none';
        document.getElementById('LG').style.display = 'none';
        document.getElementById('BlackBerry').style.display = 'none';
        document.getElementById('Lenovo').style.display = 'none';
        document.getElementById('HTC').style.display = 'none';
        document.getElementById('Huawei').style.display = 'none';
        document.getElementById('Microsoft').style.display = 'none';
        document.getElementById('Другие бренды').style.display = 'none';
        document.getElementById('Asus').style.display = 'none';
    }
    if (document.getElementById("brand").value == "Nokia") {
        document.getElementById('Nokia').style.display = 'block';
        document.getElementById('Apple').style.display = 'none';
        document.getElementById('Samsung').style.display = 'none';
        document.getElementById('Sony').style.display = 'none';
        document.getElementById('LG').style.display = 'none';
        document.getElementById('BlackBerry').style.display = 'none';
        document.getElementById('Lenovo').style.display = 'none';
        document.getElementById('HTC').style.display = 'none';
        document.getElementById('Huawei').style.display = 'none';
        document.getElementById('Microsoft').style.display = 'none';
        document.getElementById('Другие бренды').style.display = 'none';
        document.getElementById('Asus').style.display = 'none';
    }

    if (document.getElementById("brand").value == "Sony") {
        document.getElementById('Sony').style.display = 'block';
        document.getElementById('Apple').style.display = 'none';
        document.getElementById('Samsung').style.display = 'none';
        document.getElementById('Nokia').style.display = 'none';
        document.getElementById('LG').style.display = 'none';
        document.getElementById('BlackBerry').style.display = 'none';
        document.getElementById('Lenovo').style.display = 'none';
        document.getElementById('HTC').style.display = 'none';
        document.getElementById('Huawei').style.display = 'none';
        document.getElementById('Microsoft').style.display = 'none';
        document.getElementById('Другие бренды').style.display = 'none';
        document.getElementById('Asus').style.display = 'none';
    }
    if (document.getElementById("brand").value == "LG"){
        document.getElementById('LG').style.display = 'block';
        document.getElementById('Apple').style.display = 'none';
        document.getElementById('Samsung').style.display = 'none';
        document.getElementById('Sony').style.display = 'none';
        document.getElementById('Nokia').style.display = 'none';
        document.getElementById('BlackBerry').style.display = 'none';
        document.getElementById('Lenovo').style.display = 'none';
        document.getElementById('HTC').style.display = 'none';
        document.getElementById('Huawei').style.display = 'none';
        document.getElementById('Microsoft').style.display = 'none';
        document.getElementById('Другие бренды').style.display = 'none';
        document.getElementById('Asus').style.display = 'none';
    }
    if (document.getElementById("brand").value == "Другие бренды"){
        document.getElementById('LG').style.display = 'none';
        document.getElementById('Apple').style.display = 'none';
        document.getElementById('Samsung').style.display = 'none';
        document.getElementById('Sony').style.display = 'none';
        document.getElementById('Nokia').style.display = 'none';
        document.getElementById('BlackBerry').style.display = 'none';
        document.getElementById('Lenovo').style.display = 'none';
        document.getElementById('HTC').style.display = 'none';
        document.getElementById('Huawei').style.display = 'none';
        document.getElementById('Microsoft').style.display = 'none';
        document.getElementById('Другие бренды').style.display = 'block';
        document.getElementById('Asus').style.display = 'none';
    }
    if (document.getElementById("brand").value == "Asus"){
        document.getElementById('LG').style.display = 'none';
        document.getElementById('Apple').style.display = 'none';
        document.getElementById('Samsung').style.display = 'none';
        document.getElementById('Sony').style.display = 'none';
        document.getElementById('Nokia').style.display = 'none';
        document.getElementById('BlackBerry').style.display = 'none';
        document.getElementById('Lenovo').style.display = 'none';
        document.getElementById('HTC').style.display = 'none';
        document.getElementById('Huawei').style.display = 'none';
        document.getElementById('Microsoft').style.display = 'none';
        document.getElementById('Другие бренды').style.display = 'none';
        document.getElementById('Asus').style.display = 'block';
    }
}

function Check_accessories() {
    if (document.getElementById("brand").value == "Чехлы"){
        document.getElementById('Чехлы').style.display = 'block';
        document.getElementById('Наушники').style.display = 'none';
        document.getElementById('Флешки').style.display = 'none';
        document.getElementById('Memory').style.display = 'none';
    }
    if (document.getElementById("brand").value == "Наушники"){
        document.getElementById('Наушники').style.display = 'block';
        document.getElementById('Чехлы').style.display = 'none';
        document.getElementById('Флешки').style.display = 'none';
        document.getElementById('Memory').style.display = 'none';
    }
    if (document.getElementById("brand").value == "Флешки"){
        document.getElementById('Флешки').style.display = 'block';
        document.getElementById('Наушники').style.display = 'none';
        document.getElementById('Чехлы').style.display = 'none';
        document.getElementById('Memory').style.display = 'block';
    }
   
}

function Check_notebooks() {
    if (document.getElementById("brand").value == "Apple"){
        document.getElementById('Apple').style.display = 'block';
        document.getElementById('Asus').style.display = 'none';
        document.getElementById('Acer').style.display = 'none';
        document.getElementById('Dell').style.display = 'none';
        document.getElementById('Samsung').style.display = 'none';
        document.getElementById('Sony').style.display = 'none';
        document.getElementById('Lenovo').style.display = 'none';
        document.getElementById('HP').style.display = 'none';
        document.getElementById('Toshiba').style.display = 'none';
        document.getElementById('Другие бренды').style.display = 'none';
    }
    if (document.getElementById("brand").value == "Asus"){
        document.getElementById('Apple').style.display = 'none';
        document.getElementById('Asus').style.display = 'block';
        document.getElementById('Acer').style.display = 'none';
        document.getElementById('Dell').style.display = 'none';
        document.getElementById('Samsung').style.display = 'none';
        document.getElementById('Sony').style.display = 'none';
        document.getElementById('Lenovo').style.display = 'none';
        document.getElementById('HP').style.display = 'none';
        document.getElementById('Toshiba').style.display = 'none';
        document.getElementById('Другие бренды').style.display = 'none';
    }
    if (document.getElementById("brand").value == "Acer"){
        document.getElementById('Apple').style.display = 'none';
        document.getElementById('Asus').style.display = 'none';
        document.getElementById('Acer').style.display = 'block';
        document.getElementById('Dell').style.display = 'none';
        document.getElementById('Samsung').style.display = 'none';
        document.getElementById('Sony').style.display = 'none';
        document.getElementById('Lenovo').style.display = 'none';
        document.getElementById('HP').style.display = 'none';
        document.getElementById('Toshiba').style.display = 'none';
        document.getElementById('Другие бренды').style.display = 'none';
    }
    if (document.getElementById("brand").value == "Dell"){
        document.getElementById('Apple').style.display = 'none';
        document.getElementById('Asus').style.display = 'none';
        document.getElementById('Acer').style.display = 'none';
        document.getElementById('Dell').style.display = 'block';
        document.getElementById('Samsung').style.display = 'none';
        document.getElementById('Sony').style.display = 'none';
        document.getElementById('Lenovo').style.display = 'none';
        document.getElementById('HP').style.display = 'none';
        document.getElementById('Toshiba').style.display = 'none';
        document.getElementById('Другие бренды').style.display = 'none';
    }
    if (document.getElementById("brand").value == "Samsung"){
        document.getElementById('Apple').style.display = 'none';
        document.getElementById('Asus').style.display = 'none';
        document.getElementById('Acer').style.display = 'none';
        document.getElementById('Dell').style.display = 'none';
        document.getElementById('Samsung').style.display = 'block';
        document.getElementById('Sony').style.display = 'none';
        document.getElementById('Lenovo').style.display = 'none';
        document.getElementById('HP').style.display = 'none';
        document.getElementById('Toshiba').style.display = 'none';
        document.getElementById('Другие бренды').style.display = 'none';
    }
    if (document.getElementById("brand").value == "Sony"){
        document.getElementById('Apple').style.display = 'none';
        document.getElementById('Asus').style.display = 'none';
        document.getElementById('Acer').style.display = 'none';
        document.getElementById('Dell').style.display = 'none';
        document.getElementById('Samsung').style.display = 'none';
        document.getElementById('Sony').style.display = 'block';
        document.getElementById('Lenovo').style.display = 'none';
        document.getElementById('HP').style.display = 'none';
        document.getElementById('Toshiba').style.display = 'none';
        document.getElementById('Другие бренды').style.display = 'none';
    }
    if (document.getElementById("brand").value == "Lenovo"){
        document.getElementById('Apple').style.display = 'none';
        document.getElementById('Asus').style.display = 'none';
        document.getElementById('Acer').style.display = 'none';
        document.getElementById('Dell').style.display = 'none';
        document.getElementById('Samsung').style.display = 'none';
        document.getElementById('Sony').style.display = 'none';
        document.getElementById('Lenovo').style.display = 'block';
        document.getElementById('HP').style.display = 'none';
        document.getElementById('Toshiba').style.display = 'none';
        document.getElementById('Другие бренды').style.display = 'none';
    }
    if (document.getElementById("brand").value == "HP"){
        document.getElementById('Apple').style.display = 'none';
        document.getElementById('Asus').style.display = 'none';
        document.getElementById('Acer').style.display = 'none';
        document.getElementById('Dell').style.display = 'none';
        document.getElementById('Samsung').style.display = 'none';
        document.getElementById('Sony').style.display = 'none';
        document.getElementById('Lenovo').style.display = 'none';
        document.getElementById('HP').style.display = 'block';
        document.getElementById('Toshiba').style.display = 'none';
        document.getElementById('Другие бренды').style.display = 'none';
    }

    if (document.getElementById("brand").value == "Toshiba"){
        document.getElementById('Apple').style.display = 'none';
        document.getElementById('Asus').style.display = 'none';
        document.getElementById('Acer').style.display = 'none';
        document.getElementById('Dell').style.display = 'none';
        document.getElementById('Samsung').style.display = 'none';
        document.getElementById('Sony').style.display = 'none';
        document.getElementById('Lenovo').style.display = 'none';
        document.getElementById('HP').style.display = 'none';
        document.getElementById('Toshiba').style.display = 'block';
        document.getElementById('Другие бренды').style.display = 'none';
    }
    if (document.getElementById("brand").value == "Другие бренды"){
        document.getElementById('Apple').style.display = 'none';
        document.getElementById('Asus').style.display = 'none';
        document.getElementById('Acer').style.display = 'none';
        document.getElementById('Dell').style.display = 'none';
        document.getElementById('Samsung').style.display = 'none';
        document.getElementById('Sony').style.display = 'none';
        document.getElementById('Lenovo').style.display = 'none';
        document.getElementById('HP').style.display = 'none';
        document.getElementById('Toshiba').style.display = 'none';
        document.getElementById('Другие бренды').style.display = 'block';
    }
}


