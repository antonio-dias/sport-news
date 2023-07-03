package com.sportnews.api.service;

import java.util.List;

import org.springframework.stereotype.Service;

import com.sportnews.api.dto.GameDto;
import com.sportnews.api.repository.GameRepository;

import lombok.RequiredArgsConstructor;

@RequiredArgsConstructor
@Service
public class GameService {
	
	private final GameRepository gameRepository;
	
	public String save(final GameDto game) {
		return gameRepository.save(game).getId();
	}
	
	public List<GameDto> findAll() {
		List<GameDto> games = gameRepository.findAll();
		return games;
	}

}
