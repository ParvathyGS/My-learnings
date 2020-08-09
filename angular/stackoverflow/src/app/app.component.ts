import { Component } from '@angular/core';
import { QuestionsService } from './questions.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  title = 'Stackoverflow';

  constructor(
    private questionService:QuestionsService,
  ) { }

  ngOnInit() {
  
  }

  Myfunc() {
    this.questionService.LoggedOut();
  }
}
