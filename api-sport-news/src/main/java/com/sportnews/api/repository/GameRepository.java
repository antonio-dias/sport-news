package com.sportnews.api.repository;

import org.springframework.data.mongodb.repository.MongoRepository;

import com.sportnews.api.dto.GameDto;

public interface GameRepository extends MongoRepository<GameDto, String>{

}
