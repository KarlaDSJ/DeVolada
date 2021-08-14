import { TestBed } from '@angular/core/testing';

import { MetodoPagoGuard } from './metodo-pago.guard';

describe('MetodoPagoGuard', () => {
  let guard: MetodoPagoGuard;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    guard = TestBed.inject(MetodoPagoGuard);
  });

  it('should be created', () => {
    expect(guard).toBeTruthy();
  });
});
