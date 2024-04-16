/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
     
    var a = function(val1){
        if (val=== val1){
            return true
        } throw new Error ("Not Equal")
    }
    var b = function(val2){
        if (val !== val2){
            return true
        } throw new Error ("Equal")
    }
    return {
        toBe: a,
        notToBe: b

    }
}
    


/**
; // true
 * expect(5).notToBe(5); // throws "Equal"
 */