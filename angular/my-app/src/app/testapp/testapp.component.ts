import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-testapp',
  templateUrl: './testapp.component.html',
  styleUrls: ['./testapp.component.css']
})
export class TestappComponent implements OnInit {
  data = "New component test created..."
  constructor() { }

  ngOnInit() {
  }

}
