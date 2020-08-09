import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { SignupComponent } from './signup/signup.component';
import { QuestionsComponent } from './questions/questions.component';
import { AskquestionsComponent } from './askquestions/askquestions.component';
import { ShowquestionComponent }  from './showquestion/showquestion.component';
import { AnswerComponent }  from './answer/answer.component';
import { MyquestionsComponent }  from './myquestions/myquestions.component';
import { EditanswerComponent }  from './editanswer/editanswer.component';
import { DeleteanswerComponent }  from './deleteanswer/deleteanswer.component';
import { EditquestionComponent }  from './editquestion/editquestion.component';
import { AnswersbymeComponent }  from './answersbyme/answersbyme.component';
import { QuestionsearchComponent }  from './questionsearch/questionsearch.component';
import { DeletequestionComponent }  from './deletequestion/deletequestion.component';
import { LikequestionComponent }  from './likequestion/likequestion.component';
import { DislikequestionComponent }  from './dislikequestion/dislikequestion.component';


const routes: Routes = [
  {path : 'login', component : LoginComponent },
  {path : 'signup', component : SignupComponent },
  {path : 'question', component : QuestionsComponent },
  {path : 'ask-questions', component : AskquestionsComponent },
  {path : 'show-question/:id', component : ShowquestionComponent },
  {path : 'answer-question/:id', component : AnswerComponent},
  {path : 'myquestions', component : MyquestionsComponent },
  {path : 'editanswer/:id', component : EditanswerComponent },
  {path : 'deleteanswer/:id', component : DeleteanswerComponent },
  {path : 'editquestion/:id', component : EditquestionComponent },
  {path : 'answersbyme', component : AnswersbymeComponent },
  {path : 'questionsearch', component : QuestionsearchComponent },
  {path : 'deletequestion/:id', component : DeletequestionComponent },
  {path : 'likequestion/:id', component : LikequestionComponent },
  {path : 'dislikequestion/:id', component : DislikequestionComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})

export class AppRoutingModule { }
