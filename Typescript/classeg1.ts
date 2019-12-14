class Car {
    engine:string

    constructor(engine:string) {
        this.engine = engine
    }

    disp() : void {
        console.log("function is " + this.engine)
    }
}
    var obj = new Car("Vento")
    console.log("REading the field value of engine as " + obj.engine)
    obj.disp()

