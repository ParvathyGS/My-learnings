import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClientModule }    from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { SignupComponent } from './signup/signup.component';
import { QuestionsComponent } from './questions/questions.component';
import { MessagesComponent } from './messages/messages.component';
import { AskquestionsComponent } from './askquestions/askquestions.component';
import { ShowquestionComponent } from './showquestion/showquestion.component';
import { AnswerComponent } from './answer/answer.component';
import { MyquestionsComponent } from './myquestions/myquestions.component';
import { EditanswerComponent } from './editanswer/editanswer.component';
import { DeleteanswerComponent } from './deleteanswer/deleteanswer.component';
import { EditquestionComponent } from './editquestion/editquestion.component';
import { AnswersbymeComponent } from './answersbyme/answersbyme.component';
import { QuestionsearchComponent } from './questionsearch/questionsearch.component';
import { DeletequestionComponent } from './deletequestion/deletequestion.component';
import { LikequestionComponent } from './likequestion/likequestion.component';
import { DislikequestionComponent } from './dislikequestion/dislikequestion.component';


@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    SignupComponent,
    QuestionsComponent,
    MessagesComponent,
    AskquestionsComponent,
    ShowquestionComponent,
    AnswerComponent,
    MyquestionsComponent,
    EditanswerComponent,
    DeleteanswerComponent,
    EditquestionComponent,
    AnswersbymeComponent,
    QuestionsearchComponent,
    DeletequestionComponent,
    LikequestionComponent,
    DislikequestionComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
