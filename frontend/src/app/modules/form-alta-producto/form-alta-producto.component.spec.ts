import { ComponentFixture, TestBed } from '@angular/core/testing';
import { NgbActiveModal, NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { FormAltaProductoComponent } from './form-alta-producto.component';
import { Component } from '@angular/core';
import { FormControl } from '@angular/forms';

describe('FormAltaProductoComponent', () => {
  let component: FormAltaProductoComponent;
  let fixture: ComponentFixture<FormAltaProductoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ FormAltaProductoComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(FormAltaProductoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
