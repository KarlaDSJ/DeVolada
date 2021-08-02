import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BarraNavCompradorComponent } from './barra-nav-comprador.component';

describe('BarraNavCompradorComponent', () => {
  let component: BarraNavCompradorComponent;
  let fixture: ComponentFixture<BarraNavCompradorComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ BarraNavCompradorComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(BarraNavCompradorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
