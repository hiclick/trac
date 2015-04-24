/**
 * Created with PyCharm.
 * User: Christen
 * Date: 13-4-13
 * Time: PM3:19
 * To change this template use File | Settings | File Templates.
 */

// http://my.oschina.net/feichexia/blog/122217

// IIFE Immediate Invoked Function Expression

(function() {
    var myVar = 10;
    var myFunc = function() {
        console.log(myVar);
    };
    myFunc();
})();


(function(window, document, undefined) {
    var myFunc;
    myFunc = function (var1, var2) {
        console.log(var1);
        console.log(var2);
        console.log(document.title);

    };
    window.myFunc = myFunc;
}) (window, document);

myFunc('chen','zixin');

