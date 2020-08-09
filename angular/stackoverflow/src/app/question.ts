export class Question_details {
    questions? : Array<Question>;
    id? : number;
    data? : Array<Question>;
    first_page_url?: string;
}

export class Question {
    id? : number;
    user_id? : number;
    title? : string;
    question? : string;
    created_at? : Date;
    updated_at? :  Date;
    answers? : Array<Answer>;
    message?: string;
    token? : string;
    
}

export class Questions {
    current_page? : number;
    data? : Array<Question>;
    first_page_url? : string;
    from? : number;
    last_page? : number;
    last_page_url? :  string;
    
}

export class Answer {
    id? : number;
    user_id? : number;
    question_id? : number;
    answer? : string;
    created_at? : Date;
    updated_at? :  Date;
    // user : Users;
}

// export class Users {
//     id? : number;
//     name? : string;
//     email? : string;
//     created_at? : Date;
//     updated_at? :  Date;
// }