import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Question,Question_details, Answer } from './question';
import { MessageService} from './message.service';
import { Router } from '@angular/router';
import { catchError, map, tap } from 'rxjs/operators';

const httpOptions = {
  headers: new HttpHeaders({ //'Content-Type' : 'application/json',
                          'Authorization' : 'Bearer '+localStorage.getItem("userToken"),
                          'Authorization1' : 'Bearer '+localStorage.getItem("userId"),
                          'Authorization2' : 'Bearer '+localStorage.getItem("AnsuserId"), })
};

@Injectable({
  providedIn: 'root'
})

export class QuestionsService {

  constructor(
    private http: HttpClient,
    private messageService : MessageService,
    private router: Router,
  ) { }
  
private askUrl = 'http://forum.mashuptest.com/api/question';
private showUrl = 'http://forum.mashuptest.com/api/question';
private ansUrl = 'http://forum.mashuptest.com/api/question';
private myquestionUrl = 'http://forum.mashuptest.com/api/question/my-questions';
private editUrl = 'http://forum.mashuptest.com/api/answer';
private delUrl = 'http://forum.mashuptest.com/api/answer';
private editQuesUrl = 'http://forum.mashuptest.com/api/question';
private delQuestionUrl = 'http://forum.mashuptest.com/api/question';
private ansbymeUrl = 'http://forum.mashuptest.com/api/question/answered-by-me';
private searchUrl = 'http://forum.mashuptest.com/api/question/search?keyword=';
private likeUrl = 'http://forum.mashuptest.com/api/question';
private dislikeUrl = 'http://forum.mashuptest.com/api/question';

getuserId() {
  return localStorage.getItem('userId');
}

isLoggedIn() {
  return localStorage.getItem('userToken');
}

LoggedOut() {
  console.log("logout");
  return localStorage.removeItem('userToken');
}

AskQuestion(asked_question : Question): Observable<Question> {
  return this.http.post<Question>(this.askUrl,asked_question,httpOptions);
}

showQuestion(id : number): Observable<Question> {
  const url =`${this.showUrl}/${id}`;
  return this.http.get<Question>(url).pipe(
    tap(_ => this.log('fetched question')),
    catchError(this.handleError<Question>(`showQuestion id=${id}`))
  );
}

AddAnswer(answer_arr,id): Observable<any> {
  // console.log(answer_arr);
  // console.log(id);
  const url =`${this.ansUrl}/${id}/answer`;
  return this.http.post(url, answer_arr, httpOptions).pipe(
    tap(_ => this.log(`updated answer id=${id}`)),
    catchError(this.handleError<any>('AddAnswer'))
  );
}

MyQuestion() : Observable<any>{
  return this.http.get<any>(this.myquestionUrl,httpOptions);
}

EditAnswer(answer_arr,id): Observable<any> {
  // console.log(answer_arr);
  // console.log(id);
  const url =`${this.editUrl}/${id}`;
  return this.http.put(url, answer_arr, httpOptions).pipe(
    tap(_ => this.log(`updated answer id=${id}`)),
    catchError(this.handleError<any>('EditAnswer'))
  );
}

DeleteAnswer(answer : Answer,id) : Observable<any> {
  const url = `${this.delUrl}/${id}`;
  console.log("abc");
  console.log(id);
  return this.http.delete(url, httpOptions).pipe(
    tap(_ => this.log(`deleted answer id=${id}`)),
    catchError(this.handleError<any>('DeleteAnswer'))
  );
}

EditQuestion(question,id): Observable<any> {
  const url =`${this.editQuesUrl}/${id}`;
  return this.http.put(url, question, httpOptions).pipe(
    tap(_ => this.log(`updated question id=${id}`)),
    catchError(this.handleError<any>('EditQuestion'))
  );
}

DeleteQuestion(question : Question,id) : Observable<any> {
  console.log("abc");
  console.log(id);
  const url = `${this.delQuestionUrl}/${id}`;
  return this.http.delete(url, httpOptions).pipe(
    tap(_ => this.log(`deleted question id=${id}`)),
    catchError(this.handleError<any>('DeleteQuestion'))
  );
}

MyAnswers() : Observable<any>{
  return this.http.get<any>(this.ansbymeUrl,httpOptions);

}

QuestionSearch(keyvalue) : Observable<any> {
  const url = `${this.searchUrl}${keyvalue.keyvalue}`;
  console.log(url);
  return this.http.get<any>(url,keyvalue);
}

LikeQuestion(likeCount,id):Observable<any> {
  const url = `${this.likeUrl}/${id}/like`;
  console.log(url);
  return this.http.post<any>(url,likeCount,httpOptions).pipe(
    tap(_ => this.log(`question id=${id}`)),
    catchError(this.handleError<any>('LikeQuestion'))
  );
}

DislikeQuestion(dislikeCount,id):Observable<any> {
  const url = `${this.dislikeUrl}/${id}/remove-like`;
  console.log(url);
  return this.http.post<any>(url,dislikeCount,httpOptions).pipe(
    tap(_ => this.log(`question id=${id}`)),
    catchError(this.handleError<any>('DislikeQuestion'))
  );
}

private handleError<T> (operation = 'operation', result?: T) {
  return (error: any): Observable<T> => {

    // TODO: send the error to remote logging infrastructure
    console.error(error); // log to console instead

    // TODO: better job of transforming error for user consumption
    this.log(`${operation} failed: ${error.message}`);

    // Let the app keep running by returning an empty result.
    return of(result as T);
  };
}

log(message:string){
  this.messageService.add(message);
}

}
