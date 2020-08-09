import { Component, OnInit } from '@angular/core';
import { QuestionsService } from '../questions.service';
import { Answer, Question } from '../question';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';

@Component({
  selector: 'app-deleteanswer',
  templateUrl: './deleteanswer.component.html',
  styleUrls: ['./deleteanswer.component.css']
})
export class DeleteanswerComponent implements OnInit {

  constructor(
    private questionService : QuestionsService,
    private route: ActivatedRoute,
    private location: Location,
  ) { }

  ngOnInit() {
    this.deleteAnswer(); 
    
  }

  
goBack(): void{
  this.location.back();
}

answer : Answer;

deleteAnswer() {
  const id = +this.route.snapshot.paramMap.get('id');
  this.questionService.DeleteAnswer(this.answer,id).subscribe(()=>this.goBack());
}
}
