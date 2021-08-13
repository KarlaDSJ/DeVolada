import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BarraNavLogComponent } from './barra-nav-log.component';

describe('BarraNavLogComponent', () => {
  let component: BarraNavLogComponent;
  let fixture: ComponentFixture<BarraNavLogComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ BarraNavLogComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(BarraNavLogComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
