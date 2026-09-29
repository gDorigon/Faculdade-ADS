import { SafeAreaView, StyleSheet, Text } from "react-native";

export default function TelaHome(navigation) {
  return (
    <SafeAreaView style={estilos.tela}>
      <Text style={estilos.titulo}>Home</Text>
    </SafeAreaView>
  );
}

const estilos = StyleSheet.create({
  tela: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    padding: 24,
    backgroundColor: "#fff",
  },
  titulo: {
    fontSize: 24,
    fontWeight: "bold",
    color: "#21295C",
  },
});
