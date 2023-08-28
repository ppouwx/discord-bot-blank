TARGET = bot.py
EXE_TARGET = botrunner.exe
COMMON_SOURCES = libraries.py tokens.py prefixandtypes.py wordofthedayjson.py botactivity.py commandslist.py botstats.py picrandomizer.py rock-paper-scissors-game.py wordoftheday.py actionsuser.py emptyembedmessage.py addictionalfunctions.py ending.py
RUNNER_SOURCE = runner.py

ifeq ($(filter base_openai,$(MAKECMDGOALS)),chatgpt)
    SOURCES = $(COMMON_SOURCES) chatgpt.py
else
    SOURCES = $(COMMON_SOURCES)
endif

all: $(TARGET)

$(TARGET): $(SOURCES)
	cat $(SOURCES) > $(TARGET)

$(EXE_TARGET): $(RUNNER_SOURCE)
	cp $(RUNNER_SOURCE) $(EXE_TARGET)

.PHONY: bot_launcher
bot_launcher: $(EXE_TARGET)

.PHONY: clean
clean:
	rm -f $(TARGET) $(EXE_TARGET)