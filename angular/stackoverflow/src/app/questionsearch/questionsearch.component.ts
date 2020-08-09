import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { QuestionsService } from '../questions.service';
import { Question_details,Questions } from '../question';

@Component({
  selector: 'app-questionsearch',
  templateUrl: './questionsearch.component.html',
  styleUrls: ['./questionsearch.component.css']
})
export class QuestionsearchComponent implements OnInit {

  constructor(
    private questionService:QuestionsService,
    private route: ActivatedRoute,
  ) { }

ngOnInit() {
 
  }

question_arr : Question_details[];

questionSearch(keyvalue : string){
  this.questionService.QuestionSearch(keyvalue).subscribe(result =>
    { 
      this.question_arr = result.result,
      console.log(result.result);
    }
    );
  }
}

