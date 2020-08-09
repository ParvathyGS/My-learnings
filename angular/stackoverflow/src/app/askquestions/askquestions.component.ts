import { Component, OnInit } from '@angular/core';
import { Question,Question_details } from '../question';
import { QuestionsService } from '../questions.service';
import { MessageService } from '../message.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-askquestions',
  templateUrl: './askquestions.component.html',
  styleUrls: ['./askquestions.component.css']
})
export class AskquestionsComponent implements OnInit {

  constructor(
    private router: Router,
    private questionService:QuestionsService,
    private messageService:MessageService,
  ) {}
      
    
  ngOnInit() {
    if(!this.questionService.isLoggedIn()) {
      this.router.navigate(['/login']);
    }
  }

Askquestion(asked_question : Question) { 
  // console.log(asked_question);
  this.questionService.AskQuestion(asked_question).subscribe(res => console.log(res)); 
}

}