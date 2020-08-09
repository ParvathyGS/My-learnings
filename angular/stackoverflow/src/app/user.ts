
  export class User {
    id? : number;
    name?: string;
    email?:String;
    password?: string;
    password_confirmation?:String;
    created_at?: Date;
    updated_at?: Date;
    token?:string;
    message?:string
    user? : {
      created_at? :  Date;
​​      email? : string;
​      id?: number;
​​      name? : string;
      updated_at? : Date;
    }
  }