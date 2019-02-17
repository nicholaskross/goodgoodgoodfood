import { TestBed } from '@angular/core/testing';

import { CharityService } from './charity.service';

describe('CharityService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: CharityService = TestBed.get(CharityService);
    expect(service).toBeTruthy();
  });
});
