class shape {
    Area:number

    constructor(a:number) {
        this.Area = a
    }
}

class Circle extends shape {
    disp():void {
        console.log("in child class...." + this.Area)
    }
}

var obj = new Circle(223)
obj.disp()