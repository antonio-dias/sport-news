package com.sportnews.api.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.sportnews.api.dto.GameDto;
import com.sportnews.api.service.GameService;

import lombok.RequiredArgsConstructor;

@RestController
@RequestMapping("api/games")
@RequiredArgsConstructor
public class GameController {

	@Autowired
	private GameService gameService;
	
	@PostMapping
	public ResponseEntity<String> saveGame(@RequestBody final GameDto game) {
		return ResponseEntity.ok(gameService.save(game));
	}
	
	@GetMapping
	public ResponseEntity<List<GameDto>> findAll() {
		return ResponseEntity.ok(gameService.findAll());
	}
}
