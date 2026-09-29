import { StyleSheet, View, TouchableOpacity, Text } from "react-native";
import { useVideoPlayer, VideoView } from "expo-video";

const fonte = "https://gov.br/pt-br/midias-agorabrasil/video-fundo.mp4";

export default function App() {
  const playerConf = useVideoPlayer(fonte, (p) => {
    p.loop = true;
  });

  return (
    <View style={styles.container}>
      <VideoView style={styles.video} player={playerConf} />

      <TouchableOpacity
        style={styles.botao}
        onPress={() =>
          playerConf.playing ? playerConf.pause() : playerConf.play()
        }
      >
        <Text style={styles.textoBotao}>
          {playerConf.playing ? "Teste1" : "Teste2"}
        </Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    alignItems: "center",
    justifyContent: "center",
  },

  video: {
    width: 350,
    height: 200,
  },

  botao: {
    backgroundColor: "#5e5e5e",
    padding: 12,
    borderRadius: 8,
    marginTop: 26,
  },

  textoBotao: {
    color: "#fff",
  },
});
