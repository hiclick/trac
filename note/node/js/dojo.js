/**
 * Created with PyCharm.
 * User: Christen
 * Date: 13-4-13
 * Time: PM6:45
 * To change this template use File | Settings | File Templates.
 */

var toString = {}.toString;

var isFunction = function(it){
    return toString.call(it) == "[object Function]";
};

var a = "PConline";

var b = 100;

var c = function(){};

console.log(isFunction(a));
console.log(isFunction(b));
console.log(isFunction(c));
