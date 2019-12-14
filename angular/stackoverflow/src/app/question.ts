export class Question_details {
    id? : number;
    data1? : Array<Question>;
    first_page_url?:string;

}

export class Question {
    id? : number;
    user_id? : number;
    title? : string;
    question? : string;
    token? : string;
}

