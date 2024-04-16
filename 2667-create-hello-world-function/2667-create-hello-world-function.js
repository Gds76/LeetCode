/**
 * @return {Function}
 */
var createHelloWorld = function() {
    var a = function(){
        return "Hello World"
    }
    // return function(...args) {
    //     return "Hello World"
        
    // }
    return a
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */