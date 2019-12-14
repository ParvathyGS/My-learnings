var Car = /** @class */ (function () {
    function Car(engine) {
        this.engine = engine;
    }
    Car.prototype.disp = function () {
        console.log("function is " + this.engine);
    };
    return Car;
}());
var obj = new Car("Vento");
console.log("REading the field value of engone as" + obj.engine);
obj.disp();
