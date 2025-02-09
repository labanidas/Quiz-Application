// src/store/useAuthStore.js
import { defineStore } from "pinia";
import { ref } from "vue";
import { axiosInstance } from "../lib/axios";
import { useToast } from "vue-toast-notification";

export const useAuthStore = defineStore("apiStore", () => {
  const toast = useToast();
  isSigningUp = ref(false);
  isLogginIn = ref(false);

  const register = async (data) => {
    isSigningUp.value = true;
    try {
      const response = await axiosInstance.post("/register", data);
      toast.success("Please login!", {
        position: "top-right",
        timeout: 3000,
      });
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
    isLoggingIn,
    register,
    login,
  };
});
