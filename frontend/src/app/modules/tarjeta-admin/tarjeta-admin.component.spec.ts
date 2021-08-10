import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TarjetaAdminComponent } from './tarjeta-admin.component';

describe('TarjetaAdminComponent', () => {
  let component: TarjetaAdminComponent;
  let fixture: ComponentFixture<TarjetaAdminComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TarjetaAdminComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(TarjetaAdminComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
