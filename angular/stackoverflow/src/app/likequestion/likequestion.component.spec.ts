import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { LikequestionComponent } from './likequestion.component';

describe('LikequestionComponent', () => {
  let component: LikequestionComponent;
  let fixture: ComponentFixture<LikequestionComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ LikequestionComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(LikequestionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
