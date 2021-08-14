import { TestBed } from '@angular/core/testing';

import { CompraFinalizadaGuard } from './compra-finalizada.guard';

describe('CompraFinalizadaGuard', () => {
  let guard: CompraFinalizadaGuard;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    guard = TestBed.inject(CompraFinalizadaGuard);
  });

  it('should be created', () => {
    expect(guard).toBeTruthy();
  });
});
