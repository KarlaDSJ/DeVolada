import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BarraNavVendedorComponent } from './barra-nav-vendedor.component';

describe('BarraNavVendedorComponent', () => {
  let component: BarraNavVendedorComponent;
  let fixture: ComponentFixture<BarraNavVendedorComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ BarraNavVendedorComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(BarraNavVendedorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
