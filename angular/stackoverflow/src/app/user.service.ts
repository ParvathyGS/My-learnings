import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { User } from './user';
import { MessageService} from './message.service';
import { Question, Question_details } from './question';


const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type':  'application/json', })
};

@Injectable({
  providedIn: 'root'
})

export class UserService {

  constructor(
 
    private http: HttpClient,
    private messageService : MessageService,
    ) { }

private usersUrl = 'http://forum.mashuptest.com/api/register';
private loginUrl = 'http://forum.mashuptest.com/api/login';
private askUrl = 'http://forum.mashuptest.com/api/question';
private listUrl = 'http://forum.mashuptest.com/api/question';


signupAction(credentials:User): Observable<User> {
    return this.http.post<User>(this.usersUrl,credentials);
  }

loginAction(credentials:User): Observable<User> {
  console.log(credentials);
  return this.http.post<User>(this.loginUrl,credentials);
}

// askQuestion(question:Question): Observable<Question> {
//   // console.log(question);
// }


listallQuestion(): Observable<Question_details[]> {
  return this.http.get<Question_details[]>(this.listUrl);
}
  
}
