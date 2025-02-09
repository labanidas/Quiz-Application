// src/store/useAuthStore.js
import { defineStore } from "pinia";
import { ref } from "vue";
import { axiosInstance } from "../lib/axios";
import { useToast } from "vue-toast-notification";
import { useRouter } from "vue-router";

export const useAuthStore = defineStore("apiStore", () => {
  const router = useRouter();
  const toast = useToast();
  const isSigningUp = ref(false);
  const isLogginIn = ref(false);

  const register = async (data) => {
    isSigningUp.value = true;
    try {
      const response = await axiosInstance.post("/register", data);
      toast.success("Please login!", {
        position: "top-right",
        timeout: 3000,
      });
      router.push("/login");
    } catch (error) {
      toast.error(error.message || "Something went wrong!", {
        position: "top-right",
        timeout: 3000,
      });
    } finally {
      isSigningUp.value = false;
    }
  };

  const login = async (data) => {
    isLogginIn.value = true;
    try {
      const response = await axiosInstance.post("/login", data);
      toast.success("sucess", {
        position: "top-right",
        timeout: 3000,
      });
      router.push("/dashboard");
    } catch (error) {
      toast.error(error.message || "Something went wrong!", {
        position: "top-right",
        timeout: 3000,
      });
    } finally {
      isLogginIn.value = false;
    }
  };

  return {
    isSigningUp,
    isLogginIn,
    register,
    login,
  };
});
