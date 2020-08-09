import { Component, OnInit } from '@angular/core';
import { QuestionsService } from '../questions.service';
import { Answer, Question } from '../question';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';

@Component({
  selector: 'app-deletequestion',
  templateUrl: './deletequestion.component.html',
  styleUrls: ['./deletequestion.component.css']
})
export class DeletequestionComponent implements OnInit {

  constructor(
    private questionService : QuestionsService,
    private route: ActivatedRoute,
    private location: Location,
  ) { }

  ngOnInit() {
    this.deleteQuestion();
  }

  goBack(): void{
    this.location.back();
  }
  
  question : Question;
  
  deleteQuestion() {
    
    const id = +this.route.snapshot.paramMap.get('id');
    this.questionService.DeleteQuestion(this.question,id).subscribe(()=>this.goBack());
  }
  
}
